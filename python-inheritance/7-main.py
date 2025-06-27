#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

if __name__ == "__main__":
    bg = BaseGeometry()
    try:
        bg.area()
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")
