from json_templates.recipes import recipe_shaped_bricks, recipe_shaped_dye_blocks, recipe_shaped_stairs, \
    recipe_stonecutting, recipe_shaped_wall, recipe_shaped_slab
from file_writer import *
from utils import *
from file_type_helper import *

bricks_name = "terracotta_bricks"
stairs_name = "terracotta_bricks_stairs"
slab_name = "terracotta_bricks_slab"
wall_name = "terracotta_bricks_wall"


def write_terracotta_bricks_recipes(color: str):

    # Bricks
    write_json(
        file_name=f"{color}{bricks_name}",
        content=recipe_shaped_bricks.encode(
            group=f"{bricks_name}",
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_name}"
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Bricks Stairs
    write_json(
        file_name=f"{color}{stairs_name}",
        content=recipe_shaped_stairs.encode(
            group=f"{stairs_name}",
            ingredient=f"atbyw:{color}{bricks_name}",
            result=f"atbyw:{color}{stairs_name}"
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Bricks Slab
    write_json(
        file_name=f"{color}{slab_name}",
        content=recipe_shaped_slab.encode(
            group=f"{slab_name}",
            ingredient=f"atbyw:{color}{bricks_name}",
            result=f"atbyw:{color}{slab_name}"
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

    # Recipes from dying
    if color != "":
        # Bricks from dying
        write_json(
            file_name=f"{color}{bricks_name}_from_dying",
            content=recipe_shaped_dye_blocks.encode(
                group=f"{bricks_name}",
                ingredient=f"atbyw:{bricks_name}",
                result=f"atbyw:{color}{bricks_name}",
                dye_color=color
            ),
            namespace=namespace,
            file_type=RECIPE
        )

        # Bricks Stairs from dying
        write_json(
            file_name=f"{color}{stairs_name}_from_dying",
            content=recipe_shaped_dye_blocks.encode(
                group=f"{stairs_name}",
                ingredient=f"atbyw:{stairs_name}",
                result=f"atbyw:{color}{stairs_name}",
                dye_color=color
            ),
            namespace=namespace,
            file_type=RECIPE
        )

        # Bricks Slab from dying
        write_json(
            file_name=f"{color}{slab_name}_from_dying",
            content=recipe_shaped_dye_blocks.encode(
                group=f"{slab_name}",
                ingredient=f"atbyw:{slab_name}",
                result=f"atbyw:{color}{slab_name}",
                dye_color=color
            ),
            namespace=namespace,
            file_type=RECIPE
        )

        # Bricks Wall from dying
        write_json(
            file_name=f"{color}{wall_name}_from_dying",
            content=recipe_shaped_dye_blocks.encode(
                group=f"{wall_name}",
                ingredient=f"atbyw:{wall_name}",
                result=f"atbyw:{color}{wall_name}",
                dye_color=color
            ),
            namespace=namespace,
            file_type=RECIPE
        )


def write_terracotta_bricks_stonecutting_recipes(color: str):

    # Bricks Stairs
    write_json(
        file_name=f"{color}{stairs_name}_from_{color}{bricks_name}_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"atbyw:{color}{bricks_name}",
            result=f"atbyw:{color}{stairs_name}",
            count=1
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Bricks Slab
    write_json(
        file_name=f"{color}{slab_name}_from_{color}{bricks_name}_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"atbyw:{color}{bricks_name}",
            result=f"atbyw:{color}{slab_name}",
            count=2
        ),
        namespace=namespace,
        file_type=RECIPE
    )

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
