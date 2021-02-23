from json_templates import loot_table_drop_self
from file_writer import *
from utils import *
from file_type_helper import *


def write_statue_loot_tables(animal: str):
    name = f"{animal}statue"
    wax_states = {"clean", "exposed", "dirty", "mossy", "very_mossy"}

    for wax_state in wax_states:
        full_name = f"waxed_{wax_state}_{name}"
        write_json(
            file_name=full_name,
            content=loot_table_drop_self.encode(
                loot=f"atbyw:{full_name}"
            ),
            namespace=namespace,
            file_type=LOOT_TABLE
        )

    write_json(
        file_name=name,
        content=loot_table_drop_self.encode(
                loot=f"atbyw:{name}"
        ),
        namespace=namespace,
        file_type=LOOT_TABLE
    )
