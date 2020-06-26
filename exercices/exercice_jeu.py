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
class TicTacToe :
    game_state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def checkpossible(self,indice):
        if self.game_state[indice] == " ":
            return True
        else:
            return False

    def checkPLayable(self):
        if (self.checkWin()) != "":
            return False
        else:
            return " " in self.game_state

    def checkWin(self):
        if self.game_state[0] == self.game_state[1] == self.game_state[2] and self.game_state[0] != " ":
            return self.game_state[0]
        elif self.game_state[3] == self.game_state[4] == self.game_state[5]and self.game_state[3] != " ":
            return self.game_state[3]
        elif self.game_state[6] == self.game_state[7] == self.game_state[8] and self.game_state[6] != " ":
            return self.game_state[6]
        elif self.game_state[0] == self.game_state[4] == self.game_state[8] and self.game_state[0] != " ":
            return self.game_state[0]
        elif self.game_state[2] == self.game_state[4] == self.game_state[6] and self.game_state[2] != " ":
            return self.game_state[2]
        else:
            return ""

    def printTicTacToe(self):
        line_it = 0
        line_content = "       "
        print(" --------------------------------- " )

        for case in self.game_state :
            if case != " ":
                line_content = line_content + case
            else:
                line_content = line_content + str(line_it)

            line_it =line_it + 1

            if line_it == 3 or line_it == 6 or line_it == 9:
                print(line_content)
                line_content = "       "
            else:
                line_content = line_content + "|"

        print(" --------------------------------- " )

    def checkPlayValidity(self,Position):
        if 0 <= Position <= 8:
            return self.checkpossible(Position)
        else:
            return False

    def askForPlay(self, act_player):
        cont = True
        while cont :
            print(bcolors.OKBLUE + "You again M./Mss " + act_player.player_name + bcolors.ENDC)
            print(bcolors.OKBLUE + "Your symbol is  " + act_player.player_symbol + bcolors.ENDC)
            print(bcolors.OKBLUE + "Where did U wana play ?: " + bcolors.ENDC)
            Input_Case: int = int(input(bcolors.OKGREEN + "Enter the choosen position  V "               + bcolors.ENDC))
            if self.checkPlayValidity(Input_Case):
                cont = False
                self.game_state[Input_Case]= act_player.player_symbol
                print(bcolors.OKBLUE + "This war has no end  "  + act_player.player_symbol + bcolors.ENDC)
            else:
                print(bcolors.WARNING + "Bad value" + act_player.player_symbol + bcolors.ENDC)

class Player :
    player_name = ""
    player_symbol = ""

    def askForNAme(self):
        name = input("Who dare are U ? ")
        self.player_name = name

    def askForSymbol(self):
        print(bcolors.OKBLUE + "Choose Ur Weapon : " + bcolors.ENDC)
        symbol = input(bcolors.OKGREEN + "Enter Ur Symbol V " + bcolors.ENDC)
        self.player_symbol = symbol[0]
        print("Good choice Ur " + self.player_symbol + " will cut all ur ennemies into pieces")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE + "The first challenger is Here" + bcolors.ENDC)
input(bcolors.OKGREEN + "Press enter V "               + bcolors.ENDC)
varGame = TicTacToe()

varPlayer1 = Player()
varPlayer1.askForNAme()
varPlayer1.askForSymbol()

print("Haaahh Some new blood.")

varPlayer2 = Player()
varPlayer2.askForNAme()
varPlayer2.askForSymbol()

print("")
print("")
print("")
print("")
print("")
print("")

print("Are Uready for an intense battle .")
print("Don't waste your life .")

game_cont = True
turn = 1
varGame.printTicTacToe()

while game_cont :


    if turn % 2 == 0:
        varGame.askForPlay(varPlayer1)
    else :
        varGame.askForPlay(varPlayer2)

    varGame.printTicTacToe()
    print(varGame.checkPLayable())
    if varGame.checkPLayable():

        print("Next")
        turn = turn  +1
    else:
        game_cont = False
        print("Game Over")




print(varGame.checkWin())