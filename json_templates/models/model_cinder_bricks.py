import json


def encode_block_model(orientation: int, texture_top: str, texture_side_z: str, texture_side_x: str):
    if orientation == 0:
        parent = "template_cinder_bricks"
    elif orientation == 1:
        parent = "template_horizontal_cinder_bricks"

    return json.dumps(
        {
            "parent": f"atbyw:block/concrete/cinder_bricks/{parent}",
            "textures": {
                "top": f"{texture_top}",
                "side_z": f"{texture_side_z}",
                "side_x": f"{texture_side_x}"
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


def encode_blockstates(model_horizontal: str, model_vertical: str):
    return json.dumps(
        {
            "variants": {
                "axis=x": {
                    "model": f"{model_horizontal}",
                    "x": 90,
                    "y": 90
                },
                "axis=y": {
                    "model": f"{model_vertical}"
                },
                "axis=z": {
                    "model": f"{model_horizontal}",
                    "x": 90
                }
            }
        },
        indent=4
    )
