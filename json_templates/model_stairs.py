import json


def encode_block_model(stair_shape: int, texture_bottom: str, texture_top: str, texture_side: str):
    parent = ""

    if stair_shape == 0:
        parent = "minecraft:block/stairs"
    elif stair_shape == 1:
        parent = "minecraft:block/inner_stairs"
    elif stair_shape == 2:
        parent = "minecraft:block/outer_stairs"

    return json.dumps(
        {
            "parent": f"{parent}",
            "textures": {
                "bottom": f"{texture_bottom}",
                "top": f"{texture_top}",
                "side": f"{texture_side}"
            }
        },
        indent=4
    )


def encode_item_model(parent_model: str):
    return json.dumps(
        {
            "parent": f"{parent_model}"
        },
        indent=4
    )


def encode_blockstates(model_straight: str, model_inner: str, model_outer: str):
    return json.dumps(
        {
            "variants": {
                "facing=east,half=bottom,shape=inner_left": {
                    "model": f"{model_inner}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=east,half=bottom,shape=inner_right": {
                    "model": f"{model_inner}"
                },
                "facing=east,half=bottom,shape=outer_left": {
                    "model": f"{model_outer}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=east,half=bottom,shape=outer_right": {
                    "model": f"{model_outer}"
                },
                "facing=east,half=bottom,shape=straight": {
                    "model": f"{model_straight}"
                },
                "facing=east,half=top,shape=inner_left": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=east,half=top,shape=inner_right": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=east,half=top,shape=outer_left": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=east,half=top,shape=outer_right": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=east,half=top,shape=straight": {
                    "model": f"{model_straight}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=inner_left": {
                    "model": f"{model_inner}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=inner_right": {
                    "model": f"{model_inner}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=outer_left": {
                    "model": f"{model_outer}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=outer_right": {
                    "model": f"{model_outer}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=bottom,shape=straight": {
                    "model": f"{model_straight}",
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=top,shape=inner_left": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=top,shape=inner_right": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=north,half=top,shape=outer_left": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=north,half=top,shape=outer_right": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "uvlock": True
                },
                "facing=north,half=top,shape=straight": {
                    "model": f"{model_straight}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=south,half=bottom,shape=inner_left": {
                    "model": f"{model_inner}"
                },
                "facing=south,half=bottom,shape=inner_right": {
                    "model": f"{model_inner}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=bottom,shape=outer_left": {
                    "model": f"{model_outer}"
                },
                "facing=south,half=bottom,shape=outer_right": {
                    "model": f"{model_outer}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=bottom,shape=straight": {
                    "model": f"{model_straight}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=top,shape=inner_left": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=top,shape=inner_right": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=south,half=top,shape=outer_left": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=south,half=top,shape=outer_right": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=south,half=top,shape=straight": {
                    "model": f"{model_straight}",
                    "x": 180,
                    "y": 90,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=inner_left": {
                    "model": f"{model_inner}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=inner_right": {
                    "model": f"{model_inner}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=outer_left": {
                    "model": f"{model_outer}",
                    "y": 90,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=outer_right": {
                    "model": f"{model_outer}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=bottom,shape=straight": {
                    "model": f"{model_straight}",
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=top,shape=inner_left": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=top,shape=inner_right": {
                    "model": f"{model_inner}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=west,half=top,shape=outer_left": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                },
                "facing=west,half=top,shape=outer_right": {
                    "model": f"{model_outer}",
                    "x": 180,
                    "y": 270,
                    "uvlock": True
                },
                "facing=west,half=top,shape=straight": {
                    "model": f"{model_straight}",
                    "x": 180,
                    "y": 180,
                    "uvlock": True
                }
            }
        },
        indent=4
    )
