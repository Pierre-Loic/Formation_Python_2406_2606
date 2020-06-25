# Notions à utiliser pour résoudre l'exercice :
# classes
# ______
# ENONCE
# Le but de l'exercice est de créer un jeu de morpion en lignes de commande
# en programmation orientée objet. Pour cela, on crée deux classes :
# - class TicTacToe
#     - Attributes :
#         - game_map : list
#     - Méthods :
#         - check_victory
#         - check_end
#         - check_possible
#         - update_map
#         - print_map
#         - begin_game

# - class Gamer
#     - Attributes :
#         - gamer_type : str
#         - victory_number : int
#     - Méthods :
#         - collect_move
#         - print_data


class TicTacToe:
    game_map = ["_","_","_","_","_","_","_","_","_"]
    game_type = ""
    gamers = []
    pattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    def check_victory(self):
        for i,gamer in enumerate(TicTacToe.gamers):
            for pattern in TicTacToe.pattern:
                if gamer.letter == TicTacToe.game_map[pattern[0]-1] == TicTacToe.game_map[pattern[1]-1] == TicTacToe.game_map[pattern[2]-1]:
                    return i
        return -1
    
    def check_end(self):
        for val in TicTacToe.game_map:
            if val == "_":
                return False
        return True

    def check_possible(self,move):
        if TicTacToe.game_map[move] == "_":
            return True
        return False

    def print_map(self):
        print("-----------------------")
        for i in range(int(len(TicTacToe.game_map)/3)):
            print ("|".join(TicTacToe.game_map[i*3:(i+1)*3]))
        print("-----------------------")

    def update_map(self):
        if TicTacToe.gamers[0].asPlay == False:
            move = TicTacToe.gamers[0].collect_move(TicTacToe.game_map)
            if self.check_possible(move):
                TicTacToe.game_map[move] = TicTacToe.gamers[0].letter
                TicTacToe.gamers[0].setAsPlay(True)
                TicTacToe.gamers[1].setAsPlay(False)
            else:
                print("Case déjà occuper")
                self.update_map()
        else:
            move = TicTacToe.gamers[1].collect_move(TicTacToe.game_map)
            if self.check_possible(move):
                TicTacToe.game_map[move] = TicTacToe.gamers[1].letter
                TicTacToe.gamers[1].setAsPlay(True)
                TicTacToe.gamers[0].setAsPlay(False)
            else:
                print("Case déjà occuper")
                self.update_map()

        self.print_map()
        victory = self.check_victory()
        end = self.check_end()
        if victory != -1:
            TicTacToe.gamers[victory].victory_number += 1
            print("BRAVO !")
            TicTacToe.gamers[victory].print_data()
            print("-----------------------")
            end = True
        if end:
            for gamer in TicTacToe.gamers:
                gamer.print_data()
            restart = input("Voulez-vous recommencez ? (y/n)")
            if restart.upper() == "Y":
                self.begin_game()
        else:
            self.update_map()

    def begin_game(self):
        TicTacToe.game_map = ["_","_","_","_","_","_","_","_","_"]
        for gamer in TicTacToe.gamers:
            gamer.asPlay = False
        self.update_map()
        
    def start_game(self):
        TicTacToe.game_type = input("Jouer contre l'ordinateur ?(O) ou jouer en versus(V)")
        TicTacToe.gamers.append(Gamer(input("Nom du joueur: "),False,"X"))
        if TicTacToe.game_type.upper() == "V":
            TicTacToe.gamers.append(Gamer(input("Nom du joueur 2: "),False,"O"))
            print(TicTacToe.gamers[0].gamer_name + " vs " + TicTacToe.gamers[1].gamer_name)
        else:
            pass
        self.begin_game()


class Gamer:
    def __init__(self, name, bot,letter):
        self.gamer_name = name
        self.isBot = bot
        self.victory_number = 0
        self.asPlay = False
        self.letter = letter
        if self.isBot:
            self.createBot()

    def setAsPlay(self, val):
        self.asPlay = val

    def collect_move(self,game_map):
        if self.isBot:
            pass
        else:
            print(f"joueur: {self.gamer_name}")
            move = input("Entrer un chiffre entre 1 et 9: ")
            if move.isdigit() and int(move) < 10 and int(move) > 0:
                move = int(move) - 1
                return move
            else:
                print("Erreur de saisi")
                return self.collect_move(game_map)

    def print_data(self):
        print(f"Nom: {self.gamer_name} Nombre de victoire: {self.victory_number}")

    def createBot(self):
        dif = input("Saisir une difficulté entre 1 et 3")
        if dif.isdigit() and int(dif) < 4 and int(dif) > 0:
            self.bot = Ia(dif)
        else:
            self.createBot()

class Ia:
    pattern1 = {}
    pattern2 = {}
    pattern3 = {}
    def __init__(self, difficult):
        self.difficult = int(difficult)
    
    def move(self,game_map):
        if self.difficult == 1:
            pass






game = TicTacToe()
game.start_game()