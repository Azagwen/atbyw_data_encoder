from json_templates.loot_tables import loot_table_slab_drop_self, loot_table_drop_self
from file_writer import *
from utils import *
from file_type_helper import *

stairs_name = "concrete_stairs"
slab_name = "concrete_slab"
bricks_name = "cinder_bricks"
bricks_wall_name = "cinder_blocks_wall"


def write_concrete_loot_tables(color: str):
    if color != "":
        # Stairs
        write_json(
            file_name=f"{color}{stairs_name}",
            content=loot_table_drop_self.encode(
                loot=f"atbyw:{color}{stairs_name}"
            ),
            namespace=namespace,
            file_type=LOOT_TABLE
        )
        # Slab
        write_json(
            file_name=f"{color}{slab_name}",
            content=loot_table_slab_drop_self.encode(
                loot=f"atbyw:{color}{slab_name}"
            ),
            namespace=namespace,
            file_type=LOOT_TABLE
        )
        # Bricks
        write_json(
            file_name=f"{color}{bricks_name}",
            content=loot_table_drop_self.encode(
                loot=f"atbyw:{color}{bricks_name}"
            ),
            namespace=namespace,
            file_type=LOOT_TABLE
        )
        # Bricks wall
        write_json(
            file_name=f"{color}{bricks_wall_name}",
            content=loot_table_drop_self.encode(
                loot=f"atbyw:{color}{bricks_wall_name}"
            ),
            namespace=namespace,
            file_type=LOOT_TABLE
        )
