from time import time
from ship import *


class Player():

    def __init__(self, name, is_human, ocean):
        self.name = name
        self.ocean = ocean
        self.is_human = is_human
        self.start_time = time()

    def add_ship_to_ocean(self):
        ca = Carrier(self.is_human, self.ocean)
        ba = BattleShip(self.is_human, self.ocean)
        cr = Cruiser(self.is_human, self.ocean)
        su = Submarine(self.is_human, self.ocean)
        de = Destroyer(self.is_human, self.ocean)

    def player_turn(self):
        print('Turn: ', self.name)
        print(self.ocean)
