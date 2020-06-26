from Gamers.Gamer import Gamer
from Gamers.OptiBot import OptiBot
from Gamers.RandomBot import RandomBot
from TicTacToes.TicTacToe import TicTacToe
import unittest

class TicTacToeTestsUnit(unittest.TestCase):          

    def setUp(self):
       self.ticTacToe = TicTacToe(Gamer("gamer1"),Gamer("gamer2"))

    def test_check_diags(self):  
        self.assertTrue(self.ticTacToe.check_diags(1,list([0,4,8])) == 0)
        self.assertTrue(self.ticTacToe.check_diags(0,list([0,4,8])) == 1)

    def test_1(self):  
        self.assertTrue(False is False)