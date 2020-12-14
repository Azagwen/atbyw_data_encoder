from write_terracotta import *
from write_terracotta_bricks import *
from file_writer import *
from utils import *


def encode_all():
    DirectoryWriter(namespace).create_output_dirs()
    for color in colors:
        write_terracotta_recipes(color)
        write_terracotta_bricks_recipes(color)
        write_terracotta_stonecutting_recipes(color)
        write_terracotta_bricks_stonecutting_recipes(color)


encode_all()
