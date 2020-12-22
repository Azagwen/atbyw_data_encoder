import json


def encode_block_model(wall_piece: int, texture_wall: str, texture_slab: str):
    parent = ""

    if wall_piece == 0:
        parent = "atbyw:block/concrete/cinder_bricks/wall/template_cinder_blocks_wall_post"
    elif wall_piece == 1:
        parent = "atbyw:block/concrete/cinder_bricks/wall/template_cinder_blocks_wall_side"
    elif wall_piece == 2:
        parent = "atbyw:block/concrete/cinder_bricks/wall/template_cinder_blocks_wall_side_tall"

    if wall_piece == 0 or wall_piece == 2:
        return json.dumps(
            {
                "parent": f"{parent}",
                "textures": {
                    "wall": f"{texture_wall}",
                }
            },
            indent=4
        )
    elif wall_piece == 1:
        return json.dumps(
            {
                "parent": f"{parent}",
                "textures": {
                    "wall": f"{texture_wall}",
                    "top_slab": f"{texture_slab}"
                }
            },
            indent=4
        )


def encode_item_model(parent_model: str, texture_wall: str, texture_slab: str):
    return json.dumps(
        {
            "parent": f"{parent_model}",
            "textures": {
                "wall": f"{texture_wall}",
                "top_slab": f"{texture_slab}"
            }

        },
        indent=4
    )


def encode_blockstates(model_post: str, model_side: str, model_side_tall: str):
    return json.dumps(
        {
            "multipart": [
                {
                    "when": {
                        "up": "true"
                    },
                    "apply": {
                        "model": f"{model_post}"
                    }
                },
                {
                    "when": {
                        "north": "low"
                    },
                    "apply": {
                        "model": f"{model_side}",
                    }
                },
                {
                    "when": {
                        "east": "low"
                    },
                    "apply": {
                        "model": f"{model_side}",
                        "y": 90,
                    }
                },
                {
                    "when": {
                        "south": "low"
                    },
                    "apply": {
                        "model": f"{model_side}",
                        "y": 180,
                    }
                },
                {
                    "when": {
                        "west": "low"
                    },
                    "apply": {
                        "model": f"{model_side}",
                        "y": 270,
                    }
                },
                {
                    "when": {
                        "north": "tall"
                    },
                    "apply": {
                        "model": f"{model_side_tall}",
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "east": "tall"
                    },
                    "apply": {
                        "model": f"{model_side_tall}",
                        "y": 90,
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "south": "tall"
                    },
                    "apply": {
                        "model": f"{model_side_tall}",
                        "y": 180,
                        "uvlock": True
                    }
                },
                {
                    "when": {
                        "west": "tall"
                    },
                    "apply": {
                        "model": f"{model_side_tall}",
                        "y": 270,
                        "uvlock": True
                    }
                }
            ]
        },
        indent=4
    )
