# Notions à utiliser pour résoudre l'exercice :
# classes, héritage
# ______
# ENONCE
# Le but de l'exercice est d'ajouter un fonctionnalité au jeu développé dans la
# première partie avec les deux classes : TicTacToe et Gamer.
# En utilisant l'héritage, le but est de créer une classe fille de la classe Gamer
# appelée Computer pour pouvoir jouer contre l'ordinateur 

from random import randint

class TicTacToe:
    
    def __init__(self):
        self.gamer_1 = Gamer("X")
        self.gamer_2 = Computer("O")
        self.game_map = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"],
        ]

    def begin_game(self):
        gamer = self.gamer_1
        while self.check_end() is False:
            self.print_map()
            x, y = gamer.collect_move(self.game_map)
            while self.check_possible(x, y) is False:
                x, y = gamer.collect_move(self.game_map)
            self.update_map(gamer.gamer_symbol, x, y)
            if self.check_victory(gamer.gamer_symbol) is True:
                print(f"Le joueur {gamer.gamer_symbol} a gagné la partie")
                gamer.victory_number += 1
                break
            if gamer is self.gamer_1:
                gamer = self.gamer_2
            else:
                gamer = self.gamer_1
        self.print_map()
        print("Fin de la partie")

    def check_victory(self, symbol):
        """ Check if the gamer wins the game """
        # lines
        for line in self.game_map:
            if line.count(symbol)==3:
                return True
        # columns
        for i in range(len(self.game_map)):
            if self.game_map[0][i]==self.game_map[1][i]==self.game_map[2][i]==symbol:
                return True
        # diagonal
        if self.game_map[0][0]==self.game_map[1][1]==self.game_map[2][2]==symbol:
            return True
        if self.game_map[0][2]==self.game_map[1][1]==self.game_map[2][0]==symbol:
            return True
        # else
        return False  
    
    def print_map(self):
        """ Nice printing of the map """
        print("Voici le plateau de jeu :")
        for line in self.game_map:
            print(" ".join(line))

    def update_map(self, symbol, x, y):
        """ Update the map with the new position of the gamer """
        self.game_map[y][x]=symbol

    def check_possible(self, x, y):
        """ Check if the position is not used """
        if self.game_map[y][x]=="_":
            return True
        else:
            print("Position déjà occupée")
            return False

    def check_end(self):
        """ Check if the map is full """
        for line in self.game_map:
            if "_" in line:
                return False
        else:
            return True

class Gamer:

    def __init__(self, symbol):
        self.gamer_symbol = symbol
        self.victory_number = 0

    def collect_move(self, game_map):
        pos_x = input(f"Joueur avec symbole {self.gamer_symbol}, position suivant x : ")
        while self.check_move(pos_x) is False:
            pos_x = input(f"Joueur avec symbole {self.gamer_symbol}, position suivant x : ")
        pos_y = input(f"Joueur avec symbole {self.gamer_symbol}, position suivant y : ")
        while self.check_move(pos_y) is False:
            pos_y = input(f"Joueur avec symbole {self.gamer_symbol}, position suivant y : ")
        return int(pos_x), int(pos_y)

    def check_move(self, pos):
        if pos.isdigit() is True:
            if int(pos) in range(3):
                return True
            else:
                return False
        else:
            return False

class Computer(Gamer):

    def collect_move(self, game_map):
        for i, line in enumerate(game_map):
            if line.count(self.gamer_symbol)==2 and "_" in line:
                x = line.index("_")
                y = i
                return x, y
        x, y = self.collect_random(game_map)
        return x, y

    def collect_random(self, game_map):
        pos_x = randint(0, 2)
        pos_y = randint(0, 2)
        return pos_x, pos_y

if __name__ == '__main__':
    tic = TicTacToe()
    tic.begin_game()