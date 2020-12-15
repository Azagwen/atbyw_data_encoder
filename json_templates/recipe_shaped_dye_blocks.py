import json


def encode(group: str, ingredient: str, result: str, dye_color: str):
    return json.dumps(
        {
            "type": "minecraft:crafting_shaped",
            "group": f"{group}",
            "pattern": [
                "###",
                "#B#",
                "###"
            ],
            "key": {
                "#": {
                    "item": f"{dye_color}dye"
                },
                "B": {
                    "item": f"{ingredient}"
                }
            },
            "result": {
                "item": f"{result}",
                "count": 4
            }
        },
        indent=4
    )
