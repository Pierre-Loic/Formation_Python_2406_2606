from TicTacToes.TicTacToe import TicTacToe
import time
from functools import partial
from tkinter import Label, Button, Tk
import sys
sys.setrecursionlimit(10000)

class AppTicTacToe(TicTacToe) :
    
    def construct_IHM(self):          
        Label(self.app, text='').grid(row=4, columnspan=3)
        Label(self.app, text='').grid(row=5, columnspan=3)
        Label(self.app, text='').grid(row=6,columnspan=3)

        for i in range(9):
            button = Button(self.app, text='', height=3, width=6, command=partial(self.move(i)))
            button.grid(column=i%3, row= i//3)
        self.restart_IHM()
    
    def launch_IHM(self):
        self.app.mainloop()
        
    def restart_IHM(self):
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