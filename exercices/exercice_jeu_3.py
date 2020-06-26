# Notions à utiliser pour résoudre l'exercice :
# bibliothèque tierce, tests unitaires
# ______
# ENONCE
# Le but de l'exercice est d'ajouter des tests unitaires au jeu de morpion
# pour vérifier le bon fonctionnement du jeu (avec unittest)


import random
import unittest
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
        TicTacToe.gamers.append(Gamer(input("Nom du joueur: "),"X"))
        if TicTacToe.game_type.upper() == "V":
            TicTacToe.gamers.append(Gamer(input("Nom du joueur 2: "),"O"))  
        else:
            botDif = input("Difficulté du bot entre 1 et 2")
            if botDif.isdigit() and int(botDif) < 3 and int(botDif) > 0:
                TicTacToe.gamers.append(Ia("O",int(botDif)))  
        
        print(TicTacToe.gamers[0].gamer_name + " vs " + TicTacToe.gamers[1].gamer_name)
        self.begin_game()


class Gamer:
    def __init__(self, name,letter):
        self.gamer_name = name
        self.victory_number = 0
        self.asPlay = False
        self.letter = letter

    def setAsPlay(self, val):
        self.asPlay = val

    def collect_move(self,game_map):
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

class Ia (Gamer):
    def __init__(self, letter, difficult):
        super().__init__("BOT",letter)
        self.difficult = int(difficult)
        if self.difficult == 2:
            self.medium = MediumIa(letter)

    def setAsPlay(self, val):
        self.asPlay = val

    def collect_move(self,game_map):
        print("Tour de l'ordinateur")
        
        if self.difficult == 1:
            list_tmp = []
            for i,val in enumerate(game_map):
                if val == "_":
                    list_tmp.append(i)
            return random.choice(list_tmp)
        if self.difficult == 2:
            return self.medium.play(game_map)


    def print_data(self):
        print(f"Nom: {self.gamer_name} Nombre de victoire: {self.victory_number}")

            

class MediumIa:
    pattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    def __init__(self,letter):
        self.listChoice = []
        self.listOpponentChoice = []
        self.letter = letter
        self.opponentLetter = "O" if self.letter == "X" else "X"
        self.count = 0

    def play(self, game_map):
        self.game_map = game_map
        self.trymyChoice = self.checkChoice(self.letter)
        self.tryOpponentChoice = self.checkChoice(self.opponentLetter)
        if len(self.trymyChoice) !=0:
            self.listChoice.append(random.choice(self.trymyChoice))
            return self.listChoice[-1]
        
        if len(self.tryOpponentChoice) !=0:
            self.listChoice.append(random.choice(self.tryOpponentChoice))
            return self.listChoice[-1]
        self.opponentChoice()
        if self.letter == "X": 
            return self.firstPlayer()
            pass
        else:
            return self.secondPlayer()
        self.count += 1

    def opponentChoice(self):
        for i,val in enumerate(self.game_map):
            if val == self.opponentLetter:
                self.listOpponentChoice.append(i)

    def firstPlayer(self):
        if self.count ==0:
            self.listChoice.append(random.choice([0,2,6,8]))
            return self.listChoice[-1]
        if self.count == 1:
            if self.game_map[4] == self.opponentLetter:
                if self.listChoice[-1] == 0:
                    self.listChoice.append(8)
                if self.listChoice[-1] == 2:
                    self.listChoice.append(6)
                if self.listChoice[-1] == 6:
                    self.listChoice.append(2)
                if self.listChoice[-1] == 8:
                    self.listChoice.append(0)
                return self.listChoice[-1]
        list_tmp = []
        for i,val in enumerate(self.game_map):
            if val == "_":
                list_tmp.append(i)
        self.listChoice.append(random.choice(list_tmp))
        return self.listChoice[-1]
            
    def secondPlayer(self):
        if self.count == 0:
            if self.game_map.index(self.opponentLetter) == 4:
                self.listChoice.append(random.choice([0,2,6,8]))
                return self.listChoice[-1]

            self.listChoice.append(4)
            return self.listChoice[-1]
        if self.count == 1:
            if self.listChoice[-1] == 4:
                self.listChoice.append(random.choice(filter(lambda x :x not in [1,3,5,7], self.listOpponentChoice)))
                print(self.listChoice[-1])
                #return self.listChoice[-1]

        list_tmp = []
        for i,val in enumerate(self.game_map):
            if val == "_":
                list_tmp.append(i)
        self.listChoice.append(random.choice(list_tmp))
        return self.listChoice[-1]

    def checkChoice(self,letter):
        tmpList = []
        for pattern in MediumIa.pattern:
            if letter == self.game_map[pattern[0]-1]:
                if letter == self.game_map[pattern[1]-1]:
                    if "_" == self.game_map[pattern[2]-1]:
                        tmpList.append(pattern[2]-1)
            
            if letter == self.game_map[pattern[2]-1]:
                if letter == self.game_map[pattern[1]-1]:
                    if "_" == self.game_map[pattern[0]-1]:
                        tmpList.append(pattern[0]-1)

        return tmpList
# game = TicTacToe()
# game.start_game()





class MonTest(unittest.TestCase):
    def testSecondPlayerStartCenter(self):
        game_map = ["_","_","_","_","X","_","_","_","_"]
        medium = MediumIa("O")
        self.assertIn(medium.play(game_map),[0,2,6,8])

    def testSecondPlayerStartOutside(self):
        game_map = ["_","_","_","_","_","_","_","X","_"]
        medium = MediumIa("O")
        self.assertEqual(medium.play(game_map),4)

    def testSecondPlayerStartCounter(self):
        game_map = ["_","_","_","_","_","_","_","X","X"]
        medium = MediumIa("O")
        self.assertEqual(medium.play(game_map),6)
    
    def testSecondPlayerStartCounter2(self):
        game_map = ["O","O","_","_","_","_","_","X","X"]
        medium = MediumIa("O")
        self.assertEqual(medium.play(game_map),2)

if __name__ == '__main__':
    unittest.main()