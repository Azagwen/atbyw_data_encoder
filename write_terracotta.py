from json_encoders import (
    recipe_shaped_stairs,
    recipe_shaped_slab,
    recipe_stonecutting
)
from file_writer import *
from utils import *


def write_terracotta_recipes(color: str):
    stairs_name = "terracotta_stairs"
    slab_name = "terracotta_slab"

    # Stairs
    write_json(
        file_name=f"{color}{stairs_name}",
        content=recipe_shaped_stairs.encode(
            group=f"{stairs_name}",
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{stairs_name}"
        ),
        namespace=namespace
    )

    # Slab
    write_json(
        file_name=f"{color}{slab_name}",
        content=recipe_shaped_slab.encode(
            group=f"{slab_name}",
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{slab_name}"
        ),
        namespace=namespace
    )


def write_terracotta_stonecutting_recipes(color: str):
    stairs_name = "terracotta_stairs"
    slab_name = "terracotta_slab"
    bricks_name = "terracotta_bricks"
    bricks_stairs_name = "terracotta_bricks_stairs"
    bricks_slab_name = "terracotta_bricks_slab"
    bricks_wall_name = "terracotta_bricks_wall"

    # Bricks
    write_json(
        file_name=f"{color}{bricks_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_name}",
            count=1
        ),
        namespace=namespace
    )

    # Stairs
    write_json(
        file_name=f"{color}{stairs_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{stairs_name}",
            count=1
        ),
        namespace=namespace
    )

    # Slab
    write_json(
        file_name=f"{color}{slab_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{slab_name}",
            count=2
        ),
        namespace=namespace
    )

    # Bricks Stairs
    write_json(
        file_name=f"{color}{bricks_stairs_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_stairs_name}",
            count=1
        ),
        namespace=namespace
    )

    # Bricks Slab
    write_json(
        file_name=f"{color}{bricks_slab_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_slab_name}",
            count=2
        ),
        namespace=namespace
    )

    # Bricks wall
    write_json(
        file_name=f"{color}{bricks_wall_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_wall_name}",
            count=2
        ),
        namespace=namespace
    )