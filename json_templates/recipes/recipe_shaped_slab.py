import json


def encode(group: str, ingredient: str, result: str):
    return json.dumps(
        {
            "type": "minecraft:crafting_shaped",
            "group": f"{group}",
            "pattern": [
                "###"
            ],
            "key": {
                "#": {
                    "item": f"{ingredient}"
                }
            },
            "result": {
                "item": f"{result}",
                "count": 6
            }
        },
        indent=4
    )
