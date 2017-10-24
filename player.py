from time import time
from ship import *

class Player():

    def __init__(self, name:str, is_human:bool, ocean:Ocean):
        self.ocean = ocean
        self.is_human = is_human
        self.name = name
        self.start_time = time()

    def add_ship_to_ocean(self):
        ca = Carrier(self.is_human, self.ocean, None, None)
        ba = BattleShip(self.is_human, self.ocean, None, None)
        cr = Cruiser(self.is_human, self.ocean, None, None)
        su = Submarine(self.is_human, self.ocean, None, None)
        de = Destroyer(self.is_human, self.ocean, None, None)