from Gamers.Gamer import Gamer

class OptiBot(Gamer):
    def __init__(self, name):
        self.name = name
        self.isComputer = True

    def move(self, moves, rows, cols, diags, player ):
        pass