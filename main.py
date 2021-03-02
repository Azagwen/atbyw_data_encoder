from json_writers.write_terracotta_recipes import *
from json_writers.write_terracotta_bricks_recipes import *
from json_writers.write_terracotta_loot_tables import *
from json_writers.write_concrete_models import *
from json_writers.write_cinder_bricks_models import *
from json_writers.write_concrete_recipes import *
from json_writers.write_cinder_bricks_recipes import *
from json_writers.write_concrete_loot_tables import *
from json_writers.write_statue_models import *
from json_writers.write_waxed_statue_models import *
from json_writers.write_statue_loot_tables import *
from json_writers.write_column_models import *
from file_writer import *
from json_templates.loot_tables import loot_table_drop_self
from utils import *


def write_loot_tables_from_array(blocks: list):
    DirectoryWriter(namespace).create_output_dirs()
    for block in blocks:
        write_json(
            file_name=block,
            content=loot_table_drop_self.encode(
                loot=f"atbyw:{block}"
            ),
            namespace=namespace,
            file_type=LOOT_TABLE
        )


# Below goes the function that will be ran as soon as the program is launched.
write_loot_tables_from_array([
    "granite_tiles",
    "diorite_bricks",
    "andesite_bricks",

    "purpur_tiles",
    "smooth_purpur_block",
    "chiseled_purpur_block",
    "purpur_tiles_stairs",
    "smooth_purpur_stairs",
    "purpur_tiles_slab",
    "smooth_purpur_slab",

    "granite_column",
    "diorite_column",
    "andesite_column",
    "sandstone_column",
    "chiseled_sandstone_column",
    "red_sandstone_column",
    "chiseled_red_sandstone_column",
    "purpur_column",
    "stone_bricks_column",
    "mossy_stone_bricks_column",
    "cracked_stone_bricks_column",
    "nether_bricks_column",
    "quartz_column",
    "prismarine_column",
    "blackstone_column",
])

