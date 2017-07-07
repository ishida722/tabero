import unittest
from twapi import TwApi
from tabero import Tabero

class MaTest(unittest.TestCase):
    def setUp(self):
        self.tabe = Tabero()

    def test_tw(self):
        self.tabe.GenarateFoodList()
        print(self.tabe.GetFoodList())
        print(self.tabe.PickRandomFood())




if __name__ == '__main__':
        unittest.main()
