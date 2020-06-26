from Gamers.Gamer import Gamer
from Gamers.OptiBot import OptiBot
from Gamers.RandomBot import RandomBot
import time
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

    def begin_game(self):
        self.restart()
        self.construct_IHM()   
        self.check_bot_play()
        self.launch_IHM()

    def move(self,position):
        def do_it():
            
            if position not in self.moves :
                return

            self.app.update()
            
            if self.players[int(self.isplayer1)].isComputer :
                time.sleep(.10)

            self.isplayer1 = not self.isplayer1
            self.app.children['!label3']['text'] = f"Turn of : {self.players[int(not self.isplayer1)].name}"
            self.app.children[self.button_index(position)]['text'] = self.icon(self.isplayer1)   
            if self.move_result(int(self.isplayer1),position) :
                self.restart()
                self.restart_IHM()

            self.check_bot_play()
                
        return do_it  

    def check_bot_play(self):
        if self.players[int(not self.isplayer1)].isComputer :
                pos = self.players[int(not self.isplayer1)].move(self.moves,self.players_rows,self.players_cols,self.players_diags,not self.isplayer1)
                self.app.children[self.button_index(pos)].invoke()

    def move_result(self,player,position):
        self.players_rows[player][position//3] += 1
        self.players_cols[player][position%3] += 1
        self.players_diags[player][0] += self.check_diags(position, self.diag1)
        self.players_diags[player][1] += self.check_diags(position, self.diag2)
        self.moves.remove(position)
        return self.check_victory()          

    def check_diags(self,position, diag ):
        if position in diag:
            return 1
        else : 
            return 0

    def check_victory(self):
        if 3 in self.players_rows[int(self.isplayer1)] + self.players_cols[int(self.isplayer1)] + self.players_diags[int(self.isplayer1)]:
            self.players[int(self.isplayer1)].victory_number += 1
            return True

        if len(self.moves) == 0 :
            return True

        return False

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
            
    def restart(self):
        self.isplayer1 = self.begin_player1
        self.begin_player1 = not self.begin_player1
        self.players_rows = [[0,0,0],[0,0,0]]
        self.players_cols = [[0,0,0],[0,0,0]]
        self.players_diags = [[0,0],[0,0]]
        self.moves = [0,1,2,3,4,5,6,7,8]