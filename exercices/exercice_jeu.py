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

game_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
J1 = "X"
J2 = "0"


class Player:
    player_type = ""
    victory_number = 0

    def __init__(self, player_type, victory_number):
        self.player_type = player_type
        self.victory_number = victory_number

    def play(self):
        # Get player input
        x = input("Entrez l'abscisse compris entre 1 et 3 : ")
        y = input("Entrez l'ordonnée compris entre 1 et 3 : ")
        # Check if coord is available
        # Check if beetween 1 and 3
        return [x, y]

    def print_data(self):
        pass
    pass


class Game(Player):

    game_map = list()

    def __init__(self, game_map):
        self.game_map = game_map

    def check_victory(self, player):
        # Check line
        for x in range(0, 3):
            counter = 0
            for y in range(0, 3):
                if self.game_map[x][y] == player:
                    counter += 1
                if counter == 3:
                    return player

        # Check column
        for x in range(0, 3):
            counter = 0
            for y in range(0, 3):
                if self.game_map[y][x] == player:
                    counter += 1
                if counter == 3:
                    return player

        # Check diag
        for x in range(0, 3):
            counter = 0
            if self.game_map[x][x] == player:
                counter += 1
            if counter == 3:
                return player

        return False

    def check_end(self):
        compteur = 0
        for x in range(0, 3):
            for y in range(0, 3):
                if(self.game_map[x][y] != '-'):
                    compteur += 1
        if compteur == 8:
            return True
        return False

    def display_score(self):
        print("-----------------------------------------")
        print("-----------------SCORE-------------------")
        print("-----------------------------------------")
        print(f"JOUEUR X: {player_1.victory_number}")
        print(f"JOUEUR O: {player_2.victory_number}")
        print("-----------------------------------------")
        pass

    def print_map(self):
        for x in range(0, 3):
            for y in range(0, 3):
                print("|", end="")
                print(self.game_map[x][y], end="")
            print("|")
        print("-----------------------------------------")
        pass

    def launch_game(self):
        self.game_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.print_map()
        end_of_game = False
        # Player 1 is first to play
        player_type = J1
        player = player_1
        while end_of_game == False:

            print("Joueur " + player_type + " à vous de jouer !")
            # Update game map data
            coord = Player.play(self)
            self.game_map[int(coord[0]) - 1][int(coord[1]) - 1] = player_type
            self.print_map()

            # Check end or victory
            if self.check_victory(player_type) == player_type:
                print("Joueur " + player_type + " a gagné")
                score = player.victory_number
                score += 1
                player.victory_number = score
                return player
            elif self.check_end():
                print("Égalité entre les joueurs")
                return "Egalité"
            else:
                if player_type == J1:
                    player_type = J2
                    player = player_2
                else:
                    player_type = J1
                    player = player_1

            pass
        pass

    def game(self):
        chx = "o"
        while chx == "o":
            # Display score
            game.display_score()
            # Launch new game
            game.launch_game()
            chx = input("Voulez vous rejouer ? (o)")
            pass
        pass
    pass


# Launch game and init player
player_1 = Player(J1, 0)
player_2 = Player(J2, 0)
game = Game(game_map)
game.game()
