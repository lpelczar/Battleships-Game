from time import time
from ship import *


class Player():

    def __init__(self, name, is_human, ocean):
        self.name = name
        self.ocean = ocean
        self.is_human = is_human
        self.start_time = time()

    def put_carrier_on_board(self, is_horizontal, x, y):
        Carrier(self.is_human, self.ocean, is_horizontal, (x, y))

    def put_battleship_on_board(self, is_horizontal, x, y):
        BattleShip(self.is_human, self.ocean, is_horizontal, (x, y))

    def put_cruiser_on_board(self, is_horizontal, x, y):
        Cruiser(self.is_human, self.ocean, is_horizontal, (x, y))

    def put_submarine_on_board(self, is_horizontal, x, y):
        Submarine(self.is_human, self.ocean, is_horizontal, (x, y))

    def put_destroyer_on_board(self, is_horizontal, x, y):
        Destroyer(self.is_human, self.ocean, is_horizontal, (x, y))

    def player_turn(self):
        print('Turn: ', self.name)
        print(self.ocean)
