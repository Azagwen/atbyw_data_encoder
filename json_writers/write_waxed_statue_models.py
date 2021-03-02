from json_templates.models import model_waxed_statue
from file_writer import *
from utils import *
from file_type_helper import *


def write_waxed_statue_models(animal: str):
    name = f"{animal}statue"
    levels = {0, 1, 2, 3, 4}
    prefixes = ["clean", "exposed", "dirty", "mossy", "very_mossy"]

    for level in levels:
        write_json(
            file_name=f"waxed_{prefixes[level]}_{name}",
            content=model_waxed_statue.encode_item_model(
                statue_name=name,
                level=level
            ),
            namespace=namespace,
            file_type=ITEM_MODEL
        )

        write_json(
            file_name=f"waxed_{prefixes[level]}_{name}",
            content=model_waxed_statue.encode_blockstates(
                statue_name=name,
                level=level
            ),
            namespace=namespace,
            file_type=BLOCKSTATES
        )
