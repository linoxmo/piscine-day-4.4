from alchemy import create_air


if __name__ == '__main__':
    print("=== Alembic 5===")
    print("Accessing the alchemy module using ’from alchemy import’")
    try:
        print(create_air())
    except Exception as e:
        print("Testing create_air:", e)
