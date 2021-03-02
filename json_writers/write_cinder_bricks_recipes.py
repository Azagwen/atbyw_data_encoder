from json_templates.recipes import recipe_shaped_bricks, recipe_stonecutting, recipe_shaped_wall
from file_writer import *
from utils import *
from file_type_helper import *

concrete_name = "concrete"
bricks_name = "cinder_bricks"
wall_name = "cinder_blocks_wall"


def write_cinder_bricks_recipes(color: str):
    if color != "":
        # Bricks
        write_json(
            file_name=f"{color}{bricks_name}",
            content=recipe_shaped_bricks.encode(
                group=f"{bricks_name}",
                ingredient=f"minecraft:{color}{concrete_name}",
                result=f"atbyw:{color}{bricks_name}"
            ),
            namespace=namespace,
            file_type=RECIPE
        )
        # Bricks Wall
        write_json(
            file_name=f"{color}{wall_name}",
            content=recipe_shaped_wall.encode(
                group=f"{wall_name}",
                ingredient=f"atbyw:{color}{bricks_name}",
                result=f"atbyw:{color}{wall_name}"
            ),
            namespace=namespace,
            file_type=RECIPE
        )


def write_cinder_bricks_stonecutting_recipes(color: str):
    if color != "":
        # Bricks wall
        write_json(
            file_name=f"{color}{wall_name}_from_{color}{bricks_name}_stonecutting",
            content=recipe_stonecutting.encode(
                ingredient=f"atbyw:{color}{bricks_name}",
                result=f"atbyw:{color}{wall_name}",
                count=1
            ),
            namespace=namespace,
            file_type=RECIPE
        )
