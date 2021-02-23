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
from file_writer import *
from utils import *


def encode_terracotta_data():
    DirectoryWriter(namespace).create_output_dirs()
    for color in colors:
        # write_terracotta_recipes(color)
        # write_terracotta_bricks_recipes(color)
        # write_terracotta_stonecutting_recipes(color)
        # write_terracotta_bricks_stonecutting_recipes(color)
        write_terracotta_loot_tables(color)


def encode_concrete_assets():
    DirectoryWriter(namespace).create_output_dirs()
    for color in colors:
        # write_concrete_stairs_models(color)
        # write_concrete_slab_models(color)
        # write_cinder_bricks_models(color)
        # write_cinder_blocks_walls_models(color)
        # write_concrete_recipes(color)
        # write_cinder_bricks_recipes(color)
        # write_concrete_stonecutting_recipes(color)
        # write_cinder_bricks_stonecutting_recipes(color)
        write_concrete_loot_tables(color)


def encode_statue_models():
    DirectoryWriter(namespace).create_output_dirs()
    for animal in animals:
        write_statue_models(animal)


def encode_waxed_statue_models():
    DirectoryWriter(namespace).create_output_dirs()
    for animal in animals:
        write_waxed_statue_models(animal)


def encode_statue_data():
    DirectoryWriter(namespace).create_output_dirs()
    for animal in animals:
        write_statue_loot_tables(animal)


# Below goes the function that will be ran as soon as the program is launched.
encode_terracotta_data()
encode_concrete_assets()
