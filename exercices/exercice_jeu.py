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

import time
import random
from functools import partial
from tkinter import Label, Button, Tk
import sys
sys.setrecursionlimit(10000)

class TicTacToe :
    begin_player1 = False
    isplayer1 = False
    players = []
    diag1 = [0,4,8]
    diag2 = [2,4,6]
    app = Tk()

    def __init__(self, player1, player2):           
        self.players.append(player2) 
        self.players.append(player1)  

    def check_diags(self,position, diag ):
        if position in diag:
            return 1
        else : 
            return 0

    def check_victory(self):
        if 3 in self.players_rows[int(self.isplayer1)] + self.players_cols[int(self.isplayer1)] + self.players_diags[int(self.isplayer1)]:
            self.players[int(self.isplayer1)].victory_number += 1
            self.restart()

        if len(self.moves) == 0 :
            self.restart()

    def move(self,position):
        def do_it():
            
            if position not in self.moves :
                return

            self.app.update()
            
            if self.players[int(self.isplayer1)].isComputer :
                time.sleep(.100)

            self.isplayer1 = not self.isplayer1

            self.app.children['!label3']['text'] = f"Turn of : {self.players[int(not self.isplayer1)].name}"

            self.app.children[self.button_index(position)]['text'] = self.icon(self.isplayer1)                    

            self.move_result(int(self.isplayer1),position)            

            if self.players[int(not self.isplayer1)].isComputer :
                pos = self.players[int(not self.isplayer1)].move(self.moves,self.players_rows,self.players_cols,self.players_diags,not self.isplayer1)
                self.app.children[self.button_index(pos)].invoke()
                
        return do_it

    def button_index(self,position):
        if position + 1 == 1 :
            return '!button'
        else :
            return f'!button{position + 1}'

    def icon(self, isplayer1):
        if isplayer1 :
                return 'O'                    
        else :
                return 'X'

    def move_result(self,player,position):
        self.players_rows[player][position//3] += 1
        self.players_cols[player][position%3] += 1
        self.players_diags[player][0] += self.check_diags(position, self.diag1)
        self.players_diags[player][1] += self.check_diags(position, self.diag2)
        self.moves.remove(position)
        self.check_victory()          

    def begin_game(self):  
        
        Label(self.app, text='').grid(row=4, columnspan=3)
        Label(self.app, text='').grid(row=5, columnspan=3)
        Label(self.app, text='').grid(row=6,columnspan=3)

        for i in range(9):
            button = Button(self.app, text='', height=3, width=6, command=partial(self.move(i)))
            button.grid(column=i%3, row= i//3)   

        self.restart();                   

        if self.players[int(not self.isplayer1)].isComputer :
                pos = self.players[int(not self.isplayer1)].move(self.moves,self.players_rows,self.players_cols,self.players_diags,not self.isplayer1)
                self.app.children[self.button_index(pos)].invoke()

        self.app.mainloop() 

    def restart(self):
        self.isplayer1 = self.begin_player1
        self.begin_player1 = not self.begin_player1
        self.players_rows = [[0,0,0],[0,0,0]]
        self.players_cols = [[0,0,0],[0,0,0]]
        self.players_diags = [[0,0],[0,0]]
        self.moves = [0,1,2,3,4,5,6,7,8]
        self.app.children['!label']['text'] = f"O : {self.players[1].print_data()}"
        self.app.children['!label2']['text'] = f"X : {self.players[0].print_data()}"
        self.app.children['!label3']['text'] = f"Turn of : {self.players[int(not self.isplayer1)].name}"
        self.app.children['!button']['text'] = ''
        self.app.children['!button2']['text'] = ''
        self.app.children['!button3']['text'] = ''
        self.app.children['!button4']['text'] = ''
        self.app.children['!button5']['text'] = ''
        self.app.children['!button6']['text'] = ''
        self.app.children['!button7']['text'] = ''
        self.app.children['!button8']['text'] = ''
        self.app.children['!button9']['text'] = ''

class Gamer() :
    name = ""
    isComputer = False
    victory_number = 0
    
    def __init__(self, name):
        self.name = name
        self.isComputer = False

    def print_data(self):
        return str(self.name) + " score: " + str(self.victory_number) + "\n Is bot: " + str(self.isComputer)

class RandomBot(Gamer):
    def __init__(self, name):
        self.name = name
        self.isComputer = True

    def move(self, moves, rows, cols, diags, player ):
        return random.choice(moves)

class OptiBot(Gamer):
    def __init__(self, name):
        self.name = name
        self.isComputer = True

    def move(self, moves, rows, cols, diags, player ):
        pass

gamer1 = Gamer("Nicolas")
gamer2 = Gamer("Bob")
gamer3 = RandomBot("RandomBot1")
gamer4 = RandomBot("RandomBot2")
gamer5 = OptiBot("OptiBot")

ticTacToe = TicTacToe(gamer3,gamer4)
ticTacToe.begin_game()

