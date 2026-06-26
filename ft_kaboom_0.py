import alchemy.grimoire.light_spellbook as ls


def main() -> None:
    result = ls.light_spell_record(
        "Fantasy",
        "fire, air & earth"
    )
    print(result)


if __name__ == "__main__":
    main()
