from json_templates.models import model_walls, model_cinder_bricks
from file_writer import *
from utils import *
from file_type_helper import *

cinder_bricks_name = "cinder_bricks"
cinder_blocks_wall_name = "cinder_blocks_wall"
concrete_name = "concrete"
wall_post = "_post"
wall_side = "_side"
wall_side_tall = "_side_tall"


def write_cinder_bricks_models(color):
    if color != "":
        # Block model
        write_json(
            file_name=f"{color}{cinder_bricks_name}",
            content=model_cinder_bricks.encode_block_model(
                texture_top=f"atbyw:block/{color}{cinder_bricks_name}_top",
                texture_side_z=f"atbyw:block/{color}{cinder_bricks_name}_side_z",
                texture_side_x=f"atbyw:block/{color}{cinder_bricks_name}_side_x",
                orientation=VERTICAL
            ),
            namespace=namespace,
            file_type=BLOCK_MODEL
        )
        write_json(
            file_name=f"{color}horizontal_{cinder_bricks_name}",
            content=model_cinder_bricks.encode_block_model(
                texture_top=f"atbyw:block/{color}{cinder_bricks_name}_top",
                texture_side_z=f"atbyw:block/{color}{cinder_bricks_name}_side_z",
                texture_side_x=f"atbyw:block/{color}{cinder_bricks_name}_side_x",
                orientation=HORIZONTAL
            ),
            namespace=namespace,
            file_type=BLOCK_MODEL
        )

        # Item model
        write_json(
            file_name=f"{color}{cinder_bricks_name}",
            content=model_cinder_bricks.encode_item_model(
                parent_model=f"atbyw:block/concrete/cinder_bricks/{color}{cinder_bricks_name}"
            ),
            namespace=namespace,
            file_type=ITEM_MODEL
        )

        # Blockstates
        write_json(
            file_name=f"{color}{cinder_bricks_name}",
            content=model_cinder_bricks.encode_blockstates(
                model_vertical=f"atbyw:block/concrete/cinder_bricks/{color}{cinder_bricks_name}",
                model_horizontal=f"atbyw:block/concrete/cinder_bricks/{color}horizontal_{cinder_bricks_name}"
            ),
            namespace=namespace,
            file_type=BLOCKSTATES
        )


def write_cinder_blocks_walls_models(color):
    if color != "":
        # Block model
        write_json(
            file_name=f"{color}{cinder_blocks_wall_name}{wall_post}",
            content=model_walls.encode_block_model(
                texture_wall=f"atbyw:block/{color}{cinder_bricks_name}_post",
                texture_slab="",
                wall_piece=POST
            ),
            namespace=namespace,
            file_type=BLOCK_MODEL
        )
        write_json(
            file_name=f"{color}{cinder_blocks_wall_name}{wall_side}",
            content=model_walls.encode_block_model(
                texture_wall=f"atbyw:block/{color}{cinder_bricks_name}_side_z",
                texture_slab=f"atbyw:block/{color}{cinder_bricks_name}_post",
                wall_piece=SIDE
            ),
            namespace=namespace,
            file_type=BLOCK_MODEL
        )
        write_json(
            file_name=f"{color}{cinder_blocks_wall_name}{wall_side_tall}",
            content=model_walls.encode_block_model(
                texture_wall=f"atbyw:block/{color}{cinder_bricks_name}_side_z",
                texture_slab="",
                wall_piece=SIDE_TALL
            ),
            namespace=namespace,
            file_type=BLOCK_MODEL
        )

        # Item model
        write_json(
            file_name=f"{color}{cinder_blocks_wall_name}",
            content=model_walls.encode_item_model(
                parent_model=f"atbyw:block/concrete/cinder_bricks/wall/template_{cinder_blocks_wall_name}_inventory",
                texture_wall=f"atbyw:block/{color}{cinder_bricks_name}_side_z",
                texture_slab=f"atbyw:block/{color}{cinder_bricks_name}_post"
            ),
            namespace=namespace,
            file_type=ITEM_MODEL
        )

        # Blockstates
        write_json(
            file_name=f"{color}{cinder_blocks_wall_name}",
            content=model_walls.encode_blockstates(
                model_post=f"atbyw:block/concrete/cinder_bricks/wall/{color}{cinder_blocks_wall_name}{wall_post}",
                model_side=f"atbyw:block/concrete/cinder_bricks/wall/{color}{cinder_blocks_wall_name}{wall_side}",
                model_side_tall=f"atbyw:block/concrete/cinder_bricks/wall/{color}{cinder_blocks_wall_name}{wall_side_tall}"
            ),
            namespace=namespace,
            file_type=BLOCKSTATES
        )

