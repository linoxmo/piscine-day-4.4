import alchemy.grimoire.light_spellbook as ls


def main() -> None:
    result = ls.light_spell_record(
        "fireball",
        "fire and air"
    )
    print(result)


if __name__ == "__main__":
    main()
