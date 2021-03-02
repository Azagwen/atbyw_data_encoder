from json_templates.recipes import recipe_shaped_stairs, recipe_stonecutting, recipe_shaped_slab
from file_writer import *
from utils import *
from file_type_helper import *

concrete_name = "concrete"
stairs_name = "concrete_stairs"
slab_name = "concrete_slab"
bricks_name = "cinder_bricks"
bricks_wall_name = "cinder_blocks_wall"


def write_concrete_recipes(color: str):
    if color != "":
        # Stairs
        write_json(
            file_name=f"{color}{stairs_name}",
            content=recipe_shaped_stairs.encode(
                group=f"{stairs_name}",
                ingredient=f"minecraft:{color}{concrete_name}",
                result=f"atbyw:{color}{stairs_name}"
            ),
            namespace=namespace,
            file_type=RECIPE
        )
        # Slab
        write_json(
            file_name=f"{color}{slab_name}",
            content=recipe_shaped_slab.encode(
                group=f"{slab_name}",
                ingredient=f"minecraft:{color}{concrete_name}",
                result=f"atbyw:{color}{slab_name}"
            ),
            namespace=namespace,
            file_type=RECIPE
        )


def write_concrete_stonecutting_recipes(color: str):
    if color != "":
        # Bricks
        write_json(
            file_name=f"{color}{bricks_name}_from_{color}{concrete_name}_stonecutting",
            content=recipe_stonecutting.encode(
                ingredient=f"minecraft:{color}{concrete_name}",
                result=f"atbyw:{color}{bricks_name}",
                count=1
            ),
            namespace=namespace,
            file_type=RECIPE
        )
        # Stairs
        write_json(
            file_name=f"{color}{stairs_name}_from_{color}{concrete_name}_stonecutting",
            content=recipe_stonecutting.encode(
                ingredient=f"minecraft:{color}{concrete_name}",
                result=f"atbyw:{color}{stairs_name}",
                count=1
            ),
            namespace=namespace,
            file_type=RECIPE
        )
        # Slab
        write_json(
            file_name=f"{color}{slab_name}_from_{color}{concrete_name}_stonecutting",
            content=recipe_stonecutting.encode(
                ingredient=f"minecraft:{color}{concrete_name}",
                result=f"atbyw:{color}{slab_name}",
                count=2
            ),
            namespace=namespace,
            file_type=RECIPE
        )
        # Bricks wall
        write_json(
            file_name=f"{color}{bricks_wall_name}_from_{color}{concrete_name}_stonecutting",
            content=recipe_stonecutting.encode(
                ingredient=f"minecraft:{color}{concrete_name}",
                result=f"atbyw:{color}{bricks_wall_name}",
                count=1
            ),
            namespace=namespace,
            file_type=RECIPE
        )
