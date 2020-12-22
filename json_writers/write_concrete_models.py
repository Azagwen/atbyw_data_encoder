from json_templates import (
    model_stairs,
    model_slab
)
from file_writer import *
from utils import *
from file_type_helper import *

concrete_name = "concrete"
stairs = "_stairs"
stairs_inner = "_stairs_inner"
stairs_outer = "_stairs_outer"
slab_bottom = "_slab"
slab_top = "_slab_top"


def write_concrete_stairs_models(color: str):

    # Block models
    write_json(
        file_name=f"{color}{concrete_name}{stairs}",
        content=model_stairs.encode_block_model(
            texture_top=f"minecraft:block/{color}{concrete_name}",
            texture_side=f"minecraft:block/{color}{concrete_name}",
            texture_bottom=f"minecraft:block/{color}{concrete_name}",
            stair_shape=STRAIGHT
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )
    write_json(
        file_name=f"{color}{concrete_name}{stairs_inner}",
        content=model_stairs.encode_block_model(
            texture_top=f"minecraft:block/{color}{concrete_name}",
            texture_side=f"minecraft:block/{color}{concrete_name}",
            texture_bottom=f"minecraft:block/{color}{concrete_name}",
            stair_shape=INNER
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )
    write_json(
        file_name=f"{color}{concrete_name}{stairs_outer}",
        content=model_stairs.encode_block_model(
            texture_top=f"minecraft:block/{color}{concrete_name}",
            texture_side=f"minecraft:block/{color}{concrete_name}",
            texture_bottom=f"minecraft:block/{color}{concrete_name}",
            stair_shape=OUTER
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )

    # Item model
    write_json(
        file_name=f"{color}{concrete_name}{stairs}",
        content=model_stairs.encode_item_model(
            parent_model=f"atbyw:block/concrete/stairs/{color}{concrete_name}{stairs}"
        ),
        namespace=namespace,
        file_type=ITEM_MODEL
    )

    # Block states
    write_json(
        file_name=f"{color}{concrete_name}{stairs}",
        content=model_stairs.encode_blockstates(
            model_straight=f"atbyw:block/concrete/stairs/{color}{concrete_name}{stairs}",
            model_inner=f"atbyw:block/concrete/stairs/{color}{concrete_name}{stairs_inner}",
            model_outer=f"atbyw:block/concrete/stairs/{color}{concrete_name}{stairs_outer}"
        ),
        namespace=namespace,
        file_type=BLOCKSTATES
    )


def write_concrete_slab_models(color: str):

    # Block models
    write_json(
        file_name=f"{color}{concrete_name}{slab_bottom}",
        content=model_slab.encode_block_model(
            texture_top=f"minecraft:block/{color}{concrete_name}",
            texture_side=f"minecraft:block/{color}{concrete_name}",
            texture_bottom=f"minecraft:block/{color}{concrete_name}",
            slab_type=BOTTOM
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )
    write_json(
        file_name=f"{color}{concrete_name}{slab_top}",
        content=model_slab.encode_block_model(
            texture_top=f"minecraft:block/{color}{concrete_name}",
            texture_side=f"minecraft:block/{color}{concrete_name}",
            texture_bottom=f"minecraft:block/{color}{concrete_name}",
            slab_type=TOP
        ),
        namespace=namespace,
        file_type=BLOCK_MODEL
    )

    # Item model
    write_json(
        file_name=f"{color}{concrete_name}{slab_bottom}",
        content=model_slab.encode_item_model(
            parent_model=f"atbyw:block/concrete/slab/{color}{concrete_name}{slab_bottom}"
        ),
        namespace=namespace,
        file_type=ITEM_MODEL
    )

    # Block states
    write_json(
        file_name=f"{color}{concrete_name}{slab_bottom}",
        content=model_slab.encode_blockstates(
            model_bottom=f"atbyw:block/concrete/slab/{color}{concrete_name}{slab_bottom}",
            model_double=f"minecraft:block/{color}{concrete_name}",
            model_top=f"atbyw:block/concrete/slab/{color}{concrete_name}{slab_top}"
        ),
        namespace=namespace,
        file_type=BLOCKSTATES
    )
