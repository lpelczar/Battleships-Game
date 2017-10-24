from time import time
from ship import *

class Player():

    def __init__(self, name:str, is_human:bool, ocean:Ocean):
        self.ocean = ocean
        self.is_human = is_human
        self.name = name
        self.start_time = time()

    def add_ship_to_ocean(self):
        ca = Carrier(self.is_human, self.ocean)
        ba = BattleShip(self.is_human, self.ocean)
        cr = Cruiser(self.is_human, self.ocean)
        su = Submarine(self.is_human, self.ocean)
        de = Destroyer(self.is_human, self.ocean)