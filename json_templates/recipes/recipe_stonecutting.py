import json


def encode(ingredient: str, result: str, count: int):
    return json.dumps(
        {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"{ingredient}"
            },
            "result": f"{result}",
            "count": count
        },
        indent=4
    )
