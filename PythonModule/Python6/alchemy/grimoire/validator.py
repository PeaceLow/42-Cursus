def validate_ingredients(ingredients: str) -> str:
    if "fire" in ingredients:
        return f"{ingredients} - VALID"
    elif "water" in ingredients:
        return f"{ingredients} - VALID"
    elif "earth" in ingredients:
        return f"{ingredients} - VALID"
    elif "air" in ingredients:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
