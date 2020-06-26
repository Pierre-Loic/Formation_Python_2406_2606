# Notions à utiliser pour résoudre l'exercice :
# bibliothèque tierce, tests unitaires
# ______
# ENONCE
# Le but de l'exercice est d'ajouter des tests unitaires au jeu de morpion
# pour vérifier le bon fonctionnement du jeu (avec unittest)

import copy
import random
import unittest


class Player(unittest.TestCase):
    victory_number = 0

    def __init__(self, player_type, letter, victory_number):
        self.player_type = player_type
        self.letter = letter
        self.victory_number = victory_number

    def player_move(self):
        # Get player input

        x = input("Entrez l'abscisse compris entre 1 et 3 : ")
        # Check if beetween 1 and 3
        while x.isdigit() != True or int(x) > 3 or int(x) < 1:
            print("Saisie invalide")
            x = input("Entrez l'abscisse compris entre 1 et 3 : ")

        y = input("Entrez l'ordonnée compris entre 1 et 3 : ")
        while y.isdigit() != True or int(y) > 3 or int(y) < 1:
            print("Saisie invalide")
            y = input("Entrez l'abscisse compris entre 1 et 3 : ")

        return [x, y]

    def test_player_move(self):
        self.assertIsInstance(self.player_move(), list)


class Game(unittest.TestCase):

    game_map = list()
    game_type = "VS"

    def __init__(self, game_map, game_type):
        self.game_map = game_map
        self.game_type = game_type

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

        # Check diag 1
        counter = 0
        for x in range(0, 3):
            if self.game_map[x][x] == player:
                counter += 1
            if counter == 3:
                return player

        # Check diag 2
        counter = 0
        for x in range(0, 3):
            if self.game_map[2 - x][x] == player:
                counter += 1
            if counter == 3:
                return player

        return False

    def check_end(self, game_map):
        compteur = 0
        for x in range(0, 3):
            for y in range(0, 3):
                if(game_map[x][y] != '-'):
                    compteur += 1
        if compteur == 8:
            return True
        return False

    def test_check_end(self):
        self.assertFalse(self.check_end([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]))
        self.assertTrue(self.check_end([['X', 'X', '0'], ['X', 'X', '0'], ['0', '0', '-']]))

    def display_score(self):
        print("-----------------------------------------")
        print("-----------------SCORE-------------------")
        print("-----------------------------------------")
        print(f"JOUEUR X: {player_1.victory_number}")
        print(f"JOUEUR O: {player_2.victory_number}")
        print("-----------------------------------------")
        pass

    def print_map(self):
        print("-----------------------------------------")
        for x in range(0, 3):
            for y in range(0, 3):
                print("|", end="")
                print(self.game_map[x][y], end="")
            print("|")
        print("-----------------------------------------")
        pass

    def launch_game_vs(self):
        self.print_map()
        end_of_game = False
        # Player 1 is first to play
        player_type = J1
        player = player_1
        while end_of_game == False:
            print("Joueur " + player_type + " à vous de jouer !")
            # Update game map data
            coord = player.player_move()

            # Check if coord is available
            if self.game_map[int(coord[0]) - 1][int(coord[1]) - 1] != '-':
                print("La case est déjà occupé")
                coord = player.player_move()

            self.game_map[int(coord[0]) - 1][int(coord[1]) - 1] = player_type
            self.print_map()

            # Check end or victory
            if self.check_victory(player_type) == player_type:
                print("Joueur " + player_type + " a gagné")
                score = player.victory_number
                score += 1
                player.victory_number = score
                return player
            elif self.check_end(self.game_map):
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

    def launch_game_ia(self):
        self.print_map()
        end_of_game = False
        # Player 1 is first to play
        player_type = J1
        player = player_1
        while end_of_game == False:
            print("Joueur " + player_type + " à vous de jouer !")
            # Update game map data
            coord = player.player_move()

            # Check if coord is available
            if self.game_map[int(coord[0]) - 1][int(coord[1]) - 1] != '-':
                print("La case est déjà occupé")
                coord = player.player_move()

            self.game_map[int(coord[0]) - 1][int(coord[1]) - 1] = player_type
            self.print_map()

            # Check end or victory
            if self.check_victory(player_type) == player_type:
                print("Joueur " + player_type + " a gagné")
                score = player.victory_number
                score += 1
                player.victory_number = score
                return player
            elif self.check_end(self.game_map):
                print("Égalité entre les joueurs")
                return "Egalité"
            else:
                if player_type == J1:
                    player_type = J2
                    player = player_2
                    # Selon la liste des mouvements possibles un mouvement aléatoire est joué
                    list_mvt_possible = self.moves_available(J2)
                    self.game_map = computer.ia_move(game_map, list_mvt_possible)
                    self.print_map()
                    if self.check_victory(player_type) == player_type:
                        print("Joueur " + player_type + " a gagné")
                        score = player.victory_number
                        score += 1
                        player.victory_number = score
                        return player
                    elif self.check_end(self.game_map):
                        print("Égalité entre les joueurs")
                        return "Egalité"
                    else:
                        player_type = J1
                        player = player_1

    def game(self):
        chx = "o"
        while chx == "o":
            # Display score
            self.display_score()
            # Reset board
            self.game_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            # Launch new game
            print(self.game_type)
            if self.game_type == "VS":
                self.launch_game_vs()
            else:
                self.launch_game_ia()

            chx = input("Voulez vous rejouer ? (o)")
            pass
        pass

    def moves_available(self, player):
        list_move_available = []
        for x in range(0, 3):
            for y in range(0, 3):
                # check if empty
                if (self.game_map[x][y] == "-"):
                    virtual_game_map = copy.deepcopy(self.game_map)
                    virtual_game_map[x][y] = player
                    list_move_available.append(virtual_game_map)
        return list_move_available

    # Game selection, VS or IA
    def menu(self):
        print("-----------------------------------------")
        print("Veuillez choisir un mode de jeu: ")
        print("(1) Versus")
        print("(2) Contre IA")
        print("-----------------------------------------")
        game_selection = input()
        if(int(game_selection) == 1):
            game.game_type = "VS"
        elif(int(game_selection) == 2):
            print("Veuillez selectionner un niveau de difficulté: ")
            print("(1) Facile")
            print("(2) Moyen")
            print("(3) Difficile")
            print("-----------------------------------------")
            ia_level = input()
            if(int(ia_level) >= 1) or (int(ia_level) <= 3):
                computer.level = ia_level
                game.game_type = "IA"
            else:
                print("Niveau invalide")
                self.menu()
        else:
            print("Choix invalide")
            self.menu()
        self.game()


class Computer(Player):
    victory_number = 0
    level = 1

    def __init__(self, player_type, letter, victory_number, level):
        super().__init__("BOT", letter, victory_number)
        self.level = int(level)

    def ia_move(self, game_map, list_mvt_possible):
        if computer.level == 3:
            pass
        elif computer.level == 2:
            pass
        else:
            # Play random
            if(len(list_mvt_possible) > 1):
                indice_mvt = random.randint(0, len(list_mvt_possible) - 1)
                game_map = list_mvt_possible[indice_mvt]
            else:
                game_map = list_mvt_possible[0]
        return game_map


# Launch game and init player
game_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
J1 = "X"
J2 = "0"
player_1 = Player("HUMAN", J1, 0)
player_2 = Player("HUMAN", J2, 0)
computer = Computer("BOT", J2, 0, 1)
game = Game(game_map, "VS")
game.menu()

if __name__ == "__main__":
    unittest.main()
