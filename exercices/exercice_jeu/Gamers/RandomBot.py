from Gamers.Gamer import Gamer
import random

class RandomBot(Gamer):
    def __init__(self, name):
        self.name = name
        self.isComputer = True

    def move(self, moves, rows, cols, diags, player ):
        return random.choice(moves)