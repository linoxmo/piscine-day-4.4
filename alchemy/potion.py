from .elements import create_air, create_earth
import elements as e


def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}' and {create_air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed with '{e.create_fire()}' \
    and {e.create_water()}'"
