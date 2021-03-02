import json


def encode_block_model(slab_type: int, texture_bottom: str, texture_top: str, texture_side: str):
    parent = ""

    if slab_type == 0:
        parent = "minecraft:block/slab"
    elif slab_type == 1:
        parent = "minecraft:block/slab_top"

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


def encode_blockstates(model_bottom: str, model_double: str, model_top: str):
    return json.dumps(
        {
            "variants": {
                "type=bottom": {
                    "model": f"{model_bottom}"
                },
                "type=double": {
                    "model": f"{model_double}"
                },
                "type=top": {
                    "model": f"{model_top}"
                }
            }
        },
        indent=4
    )
