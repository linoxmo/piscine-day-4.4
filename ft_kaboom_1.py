import alchemy.grimoire.dark_spellbook as ds


def main() -> None:
    result = ds.dark_spell_record(
        "eyeball",
        "fire and air"
    )
    print(result)


if __name__ == "__main__":
    main()
