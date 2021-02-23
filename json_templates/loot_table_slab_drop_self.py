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
                            "functions": [
                                {
                                    "function": "minecraft:set_count",
                                    "conditions": [
                                        {
                                            "condition": "minecraft:block_state_property",
                                            "block": f"{loot}",
                                            "properties": {
                                                "type": "double"
                                            }
                                        }
                                    ],
                                    "count": 2
                                },
                                {
                                    "function": "minecraft:explosion_decay"
                                }
                            ],
                            "name": f"{loot}"
                        }
                    ]
                }
            ]
        },
        indent=4
    )
