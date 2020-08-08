#!/usr/bin/python3
try:
    from game import Game
except ImportError:
    from .game import Game


if __name__ == "__main__":
    width = 700
    height = 700
    try:
        fullscreen = input("Would you like fullscreen? Input y or n:\n")
        rows = input("Input a number for the amount of rows:\n")
        rows = int(rows)
        if fullscreen[0].lower() == "y":
            Game(width, height, rows=rows, fullscreen=True)
        elif fullscreen[0].lower() == "n":
            Game(width, height, rows=rows)
        else:
            print(f"You input \"{fullscreen}\". Please input y or n next time")
            print("Defaulting to no fullscreen")
            Game(width, height, rows=rows)

    except:
        print(f"\nYou input \"{rows}\". Please input a positive whole number next time.")
        print("Defaulting to 20 rows:")

        if fullscreen.lower() == "y":
            Game(width, height, rows=20, fullscreen=True)
        elif fullscreen.lower() == "n":
            Game(width, height, rows=20)
        else:
            print(f"You input \"{fullscreen}\". Please input y or n next time")
            print("Defaulting to no fullscreen")
            Game(width, height, rows=20)
