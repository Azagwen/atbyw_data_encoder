from json_templates import (
    loot_table_drop_self
)
from file_writer import *
from utils import *


def write_terracotta_loot_tables(color: str):
    stairs_name = "terracotta_stairs"
    slab_name = "terracotta_slab"
    bricks_name = "terracotta_bricks"
    bricks_stairs_name = "terracotta_bricks_stairs"
    bricks_slab_name = "terracotta_bricks_slab"
    bricks_wall_name = "terracotta_bricks_wall"

    # Stairs
    write_json(
        file_name=f"{color}{stairs_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{stairs_name}"
        ),
        namespace=namespace,
        is_loot_table=True
    )

    # Slab
    write_json(
        file_name=f"{color}{slab_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{slab_name}"
        ),
        namespace=namespace,
        is_loot_table=True
    )

    # Bricks
    write_json(
        file_name=f"{color}{bricks_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_name}"
        ),
        namespace=namespace,
        is_loot_table=True
    )

    # Bricks stairs
    write_json(
        file_name=f"{color}{bricks_stairs_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_stairs_name}"
        ),
        namespace=namespace,
        is_loot_table=True
    )

    # Bricks slab
    write_json(
        file_name=f"{color}{bricks_slab_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_slab_name}"
        ),
        namespace=namespace,
        is_loot_table=True
    )

    # Bricks wall
    write_json(
        file_name=f"{color}{bricks_wall_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_wall_name}"
        ),
        namespace=namespace,
        is_loot_table=True
    )
