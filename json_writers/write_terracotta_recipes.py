from json_templates.recipes import recipe_shaped_dye_blocks, recipe_shaped_stairs, recipe_stonecutting, \
    recipe_shaped_slab
from file_writer import *
from utils import *
from file_type_helper import *

stairs_name = "terracotta_stairs"
slab_name = "terracotta_slab"
bricks_name = "terracotta_bricks"
bricks_stairs_name = "terracotta_bricks_stairs"
bricks_slab_name = "terracotta_bricks_slab"
bricks_wall_name = "terracotta_bricks_wall"


def write_terracotta_recipes(color: str):

    # Stairs
    write_json(
        file_name=f"{color}{stairs_name}",
        content=recipe_shaped_stairs.encode(
            group=f"{stairs_name}",
            ingredient=f"minecraft:{color}terracotta",
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
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{slab_name}"
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Recipes from dying
    if color != "":
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


def write_terracotta_stonecutting_recipes(color: str):

    # Bricks
    write_json(
        file_name=f"{color}{bricks_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_name}",
            count=1
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Stairs
    write_json(
        file_name=f"{color}{stairs_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{stairs_name}",
            count=1
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Slab
    write_json(
        file_name=f"{color}{slab_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{slab_name}",
            count=2
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Bricks Stairs
    write_json(
        file_name=f"{color}{bricks_stairs_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_stairs_name}",
            count=1
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Bricks Slab
    write_json(
        file_name=f"{color}{bricks_slab_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_slab_name}",
            count=2
        ),
        namespace=namespace,
        file_type=RECIPE
    )

    # Bricks wall
    write_json(
        file_name=f"{color}{bricks_wall_name}_from_{color}terracotta_stonecutting",
        content=recipe_stonecutting.encode(
            ingredient=f"minecraft:{color}terracotta",
            result=f"atbyw:{color}{bricks_wall_name}",
            count=1
        ),
        namespace=namespace,
        file_type=RECIPE
    )
