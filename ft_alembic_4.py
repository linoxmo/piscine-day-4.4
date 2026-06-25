import alchemy as al


if __name__ == '__main__':
    print("=== Alembic 4===")
    print("Accessing the alchemy module using ’import alchemy’")
    try:
        print(al.create_air())
    except Exception as e:
        print("Testing create_air:", e)
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print(al.create_earth())  # type: ignore
    except Exception as e:
        print("Testing create_earth:", e)
