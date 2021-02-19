import json


def encode_item_model(statue_name: str, level: int):
    return json.dumps(
        {
            "parent": f"atbyw:block/statues/{statue_name}_{level}"
        },
        indent=4
    )


def encode_blockstates(statue_name: str, level: int):
    return json.dumps(
        {
            "variants": {
                "facing=north": {
                    "model": f"atbyw:block/statues/{statue_name}_{level}"
                },
                "facing=south": {
                    "model": f"atbyw:block/statues/{statue_name}_{level}",
                    "y": 180
                },
                "facing=east": {
                    "model": f"atbyw:block/statues/{statue_name}_{level}",
                    "y": 90
                },
                "facing=west": {
                    "model": f"atbyw:block/statues/{statue_name}_{level}",
                    "y": 270
                }
            }
        },
        indent=4
    )
