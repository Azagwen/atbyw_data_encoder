import os

output_path = "output"
data_path = f"{output_path}/data"


def paths(namespace: str, path_index: int):
    namespace_path = f"{data_path}/{namespace}"
    recipes_path = f"{namespace_path}/recipes"
    loot_tables_path = f"{namespace_path}/loot_tables"
    loot_tables_blocks_path = f"{loot_tables_path}/blocks"

    if path_index == 0:
        return namespace_path
    elif path_index == 1:
        return recipes_path
    elif path_index == 2:
        return loot_tables_path
    elif path_index == 3:
        return loot_tables_blocks_path


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


def write_json(namespace: str, file_name: str, content: str, is_loot_table: bool):
    path_index = 1
    if is_loot_table:
        path_index = 3
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
