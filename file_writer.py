from file_type_helper import *
import os

output_path = "output"
data_path = f"{output_path}/data"
assets_path = f"{output_path}/assets"


def paths(namespace: str, path_index: int):
    data_namespace_path = f"{data_path}/{namespace}"
    recipes_path = f"{data_namespace_path}/recipes"
    loot_tables_path = f"{data_namespace_path}/loot_tables"
    loot_tables_blocks_path = f"{loot_tables_path}/blocks"

    assets_namespace_path = f"{assets_path}/{namespace}"
    blockstates_path = f"{assets_namespace_path}/blockstates"
    models_path = f"{assets_namespace_path}/models"
    block_models_path = f"{models_path}/block"
    item_models_path = f"{models_path}/item"

    if path_index == 0:
        return data_namespace_path
    elif path_index == 1:
        return recipes_path
    elif path_index == 2:
        return loot_tables_path
    elif path_index == 3:
        return loot_tables_blocks_path
    elif path_index == 4:
        return assets_namespace_path
    elif path_index == 5:
        return blockstates_path
    elif path_index == 6:
        return models_path
    elif path_index == 7:
        return block_models_path
    elif path_index == 8:
        return item_models_path


class DirectoryWriter:

    def __init__(self, namespace: str):
        self.namespace = namespace

    def create_dir(self, path: str):
        try:
            os.mkdir(path)
        except FileExistsError:
            print(f"[Notice] {path} already exists !")

    def create_output_dirs(self):
        self.create_dir(output_path)
        self.create_dir(data_path)
        self.create_dir(paths(self.namespace, 0))
        self.create_dir(paths(self.namespace, 1))
        self.create_dir(paths(self.namespace, 2))
        self.create_dir(paths(self.namespace, 3))
        self.create_dir(assets_path)
        self.create_dir(paths(self.namespace, 4))
        self.create_dir(paths(self.namespace, 5))
        self.create_dir(paths(self.namespace, 6))
        self.create_dir(paths(self.namespace, 7))
        self.create_dir(paths(self.namespace, 8))


def write_json(namespace: str, file_name: str, content: str, file_type: int):
    # file types :
    # recipe        index 1
    # loot table    index 3
    # block model   index 7
    # item model    index 8
    # blockstates   index 5

    path_index = 0
    if file_type == RECIPE:
        path_index = 1
    elif file_type == LOOT_TABLE:
        path_index = 3
    elif file_type == BLOCK_MODEL:
        path_index = 7
    elif file_type == ITEM_MODEL:
        path_index = 8
    elif file_type == BLOCKSTATES:
        path_index = 5

    try:
        file = open(f"{paths(namespace, path_index)}/{file_name}.json", "x")
        file.write(content)
        file.close()
        print(f"[Created] {paths(namespace, path_index)}/{file_name}.json")
    except FileExistsError:
        file = open(f"{paths(namespace, path_index)}/{file_name}.json", "w")
        file.write(content)
        file.close()
        print(f"[Overwritten] {paths(namespace, path_index)}/{file_name}.json")
