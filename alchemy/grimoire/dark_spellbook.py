from .dark_validator import validate_ingredients_1


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frog", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients_1(ingredients)

    if "VALID" in result:
        return f"{spell_name}: recorded"
    else:
        return f"{spell_name}: rejected"
