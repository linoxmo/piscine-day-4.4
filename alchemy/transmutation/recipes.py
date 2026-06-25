import elements as e
from .. import create_air
import alchemy as al


def lead_to_gold() -> str:

    return f"Recipe transmuting Lead to Gold: brew ’{create_air()}’ and ’\
{al.heal()}’ mixed with ’[{e.create_fire()}]"
