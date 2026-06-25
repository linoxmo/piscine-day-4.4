from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)

    if "VALID" in result:
        return f"{spell_name}: recorded"
    else:
        return f"{spell_name}: rejected"
