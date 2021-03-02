import json


def encode_top(column_name: str):
    return json.dumps(
        {
            "parent": "atbyw:block/columns/template_column_top",
            "textures": {
                "top": f"atbyw:block/{column_name}_top",
                "bottom": f"atbyw:block/{column_name}_top",
                "side": f"atbyw:block/{column_name}_side"
            }
        },
        indent=4
    )


def encode_middle(column_name: str):
    return json.dumps(
        {
            "parent": "atbyw:block/columns/template_column_middle",
            "textures": {
                "side": f"atbyw:block/{column_name}_side"
            }
        },
        indent=4
    )


def encode_bottom(column_name: str):
    return json.dumps(
        {
            "parent": "atbyw:block/columns/template_column_bottom",
            "textures": {
                "top": f"atbyw:block/{column_name}_top",
                "bottom": f"atbyw:block/{column_name}_top",
                "side": f"atbyw:block/{column_name}_side"
            }
        },
        indent=4
    )


def encode_item_model(column_name: str):
    return json.dumps(
        {
            "parent": "atbyw:block/columns/template_column_inventory",
            "textures": {
                "top": f"atbyw:block/{column_name}_top",
                "bottom": f"atbyw:block/{column_name}_top",
                "side": f"atbyw:block/{column_name}_side"
            }
        },
        indent=4
    )


def encode_blockstate(column_name: str):
    return json.dumps(
        {
            "multipart": [
                {
                    "when": {
                        "top": "true"
                    },
                    "apply": {
                        "model": f"atbyw:block/columns/{column_name}_top"
                    }
                },
                {
                    "when": {
                        "middle": "true"
                    },
                    "apply": {
                        "model": f"atbyw:block/columns/{column_name}_middle"
                    }
                },
                {
                    "when": {
                        "bottom": "true"
                    },
                    "apply": {
                        "model": f"atbyw:block/columns/{column_name}_bottom"
                    }
                }
            ]
        },
        indent=4
    )
