import json


def encode(loot: str):
    return json.dumps(
        {
            "type": "minecraft:block",
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": f"{loot}"
                        }
                    ],
                    "conditions": [{"condition": "minecraft:survives_explosion"}]
                }
            ]
        },
        indent=4
    )
