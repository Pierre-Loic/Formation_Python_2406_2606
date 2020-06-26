from Gamers.Gamer import Gamer
from Gamers.OptiBot import OptiBot
from Gamers.RandomBot import RandomBot
from TicTacToes.TicTacToe import TicTacToe
from TicTacToes.AppTicTacToe import AppTicTacToe
from TicTacToes.SiteTicTacToe import SiteTicTacToe

gamer1 = Gamer("Nicolas")
gamer2 = Gamer("Bob")
gamer3 = RandomBot("RandomBot1")
gamer4 = RandomBot("RandomBot2")
gamer5 = OptiBot("OptiBot")

ticTacToe = AppTicTacToe(gamer3,gamer4)
ticTacToe.begin_game()
