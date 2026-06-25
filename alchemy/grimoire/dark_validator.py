from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients_1(ingredients: str) -> str:

    allowed = dark_spell_allowed_ingredients()

    ingredients_lower = ingredients.lower()

    is_valid = any(
        ing in ingredients_lower
        for ing in allowed
    )

    status = "VALID" if is_valid else "INVALID"

    return f"{ingredients} - {status}"
