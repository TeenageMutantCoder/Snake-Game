#!/usr/bin/python3
try:
    from game import Game
except ImportError:
    from .game import Game


if __name__ == "__main__":
    width = 700
    height = 700
    Game(width, height, rows=30)
