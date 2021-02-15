import json


def encode_block_model(statue_name: str, level: int):
    return json.dumps(
        {
            "parent": f"atbyw:block/statues/template_{statue_name}",
            "textures": {
                "texture": f"atbyw:entity/{statue_name}/{statue_name}_{level}"
            }
        },
        indent=4
    )


def encode_item_model(statue_name: str):
    return json.dumps(
        {
            "parent": f"atbyw:block/statues/{statue_name}_0"
        },
        indent=4
    )


def encode_blockstates(statue_name: str):
    return json.dumps(
        {
            "variants": {
                "facing=north,moss_accumulation=0": {
                    "model": f"atbyw:block/statues/{statue_name}_0"
                },
                "facing=south,moss_accumulation=0": {
                    "model": f"atbyw:block/statues/{statue_name}_0",
                    "y": 180
                },
                "facing=east,moss_accumulation=0": {
                    "model": f"atbyw:block/statues/{statue_name}_0",
                    "y": 90
                },
                "facing=west,moss_accumulation=0": {
                    "model": f"atbyw:block/statues/{statue_name}_0",
                    "y": 270
                },

                "facing=north,moss_accumulation=1": {
                    "model": f"atbyw:block/statues/{statue_name}_1"
                },
                "facing=south,moss_accumulation=1": {
                    "model": f"atbyw:block/statues/{statue_name}_1",
                    "y": 180
                },
                "facing=east,moss_accumulation=1": {
                    "model": f"atbyw:block/statues/{statue_name}_1",
                    "y": 90
                },
                "facing=west,moss_accumulation=1": {
                    "model": f"atbyw:block/statues/{statue_name}_1",
                    "y": 270
                },

                "facing=north,moss_accumulation=2": {
                    "model": f"atbyw:block/statues/{statue_name}_2"
                },
                "facing=south,moss_accumulation=2": {
                    "model": f"atbyw:block/statues/{statue_name}_2",
                    "y": 180
                },
                "facing=east,moss_accumulation=2": {
                    "model": f"atbyw:block/statues/{statue_name}_2",
                    "y": 90
                },
                "facing=west,moss_accumulation=2": {
                    "model": f"atbyw:block/statues/{statue_name}_2",
                    "y": 270
                },

                "facing=north,moss_accumulation=3": {
                    "model": f"atbyw:block/statues/{statue_name}_3"
                },
                "facing=south,moss_accumulation=3": {
                    "model": f"atbyw:block/statues/{statue_name}_3",
                    "y": 180
                },
                "facing=east,moss_accumulation=3": {
                    "model": f"atbyw:block/statues/{statue_name}_3",
                    "y": 90
                },
                "facing=west,moss_accumulation=3": {
                    "model": f"atbyw:block/statues/{statue_name}_3",
                    "y": 270
                },

                "facing=north,moss_accumulation=4": {
                    "model": f"atbyw:block/statues/{statue_name}_4"
                },
                "facing=south,moss_accumulation=4": {
                    "model": f"atbyw:block/statues/{statue_name}_4",
                    "y": 180
                },
                "facing=east,moss_accumulation=4": {
                    "model": f"atbyw:block/statues/{statue_name}_4",
                    "y": 90
                },
                "facing=west,moss_accumulation=4": {
                    "model": f"atbyw:block/statues/{statue_name}_4",
                    "y": 270
                }
            }
        },
        indent=4
    )
