from json_templates import (
    loot_table_drop_self
)
from file_writer import *
from utils import *
from file_type_helper import *

stairs_name = "terracotta_stairs"
slab_name = "terracotta_slab"
bricks_name = "terracotta_bricks"
bricks_stairs_name = "terracotta_bricks_stairs"
bricks_slab_name = "terracotta_bricks_slab"
bricks_wall_name = "terracotta_bricks_wall"


def write_terracotta_loot_tables(color: str):

    # Stairs
    write_json(
        file_name=f"{color}{stairs_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{stairs_name}"
        ),
        namespace=namespace,
        file_type=LOOT_TABLE
    )

    # Slab
    write_json(
        file_name=f"{color}{slab_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{slab_name}"
        ),
        namespace=namespace,
        file_type=LOOT_TABLE
    )

    # Bricks
    write_json(
        file_name=f"{color}{bricks_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_name}"
        ),
        namespace=namespace,
        file_type=LOOT_TABLE
    )

    # Bricks stairs
    write_json(
        file_name=f"{color}{bricks_stairs_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_stairs_name}"
        ),
        namespace=namespace,
        file_type=LOOT_TABLE
    )

    # Bricks slab
    write_json(
        file_name=f"{color}{bricks_slab_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_slab_name}"
        ),
        namespace=namespace,
        file_type=LOOT_TABLE
    )

    # Bricks wall
    write_json(
        file_name=f"{color}{bricks_wall_name}",
        content=loot_table_drop_self.encode(
            loot=f"atbyw:{color}{bricks_wall_name}"
        ),
        namespace=namespace,
        file_type=LOOT_TABLE
    )
