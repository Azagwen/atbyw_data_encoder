from json_templates.models import model_column
from file_writer import *
from utils import *
from file_type_helper import *


def write_column_models(stone):
    name = f"{stone}column"

    write_json(
        file_name=f"{name}_top",
        content=model_column.encode_top(
            column_name=name,
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )
    write_json(
        file_name=f"{name}_middle",
        content=model_column.encode_middle(
            column_name=name,
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )
    write_json(
        file_name=f"{name}_bottom",
        content=model_column.encode_bottom(
            column_name=name,
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )

    write_json(
        file_name=name,
        content=model_column.encode_item_model(
            column_name=name,
        ),
        namespace=namespace,
        file_type=ITEM_MODEL
    )

    write_json(
        file_name=name,
        content=model_column.encode_blockstate(
            column_name=name,
        ),
        namespace=namespace,
        file_type=BLOCKSTATES
    )
