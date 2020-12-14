import os

output_path = "output"
data_path = f"{output_path}/data"


def namespace_path(namespace: str):
    return f"{data_path}/{namespace}"


def recipes_path(namespace: str):
    return f"{namespace_path(namespace)}/recipes"


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
        self.create_dir(namespace_path(self.namespace))
        self.create_dir(recipes_path(self.namespace))


def write_json(namespace: str, file_name: str, content: str):
    try:
        file = open(f"{recipes_path(namespace)}/{file_name}.json", "x")
        file.write(content)
        file.close()
        print(f"[Created] {recipes_path(namespace)}/{file_name}.json")
    except FileExistsError:
        file = open(f"{recipes_path(namespace)}/{file_name}.json", "w")
        file.write(content)
        file.close()
        print(f"[Overwritten] {recipes_path(namespace)}/{file_name}.json")
