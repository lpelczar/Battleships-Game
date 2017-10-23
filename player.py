from time import time
from ship import *

class Player():

    def __init__(self, name:str, is_human:bool, ocean:Ocean):
        self.name = name
        self.start_time = time()

    def add_ship_to_ocean(self):
        ca = Carrier(self.is_human)
        ba = BattleShip(self.is_human)
        cr = Cruiser(self.is_human)
        su = Submarine(self.is_human)
        de = Destroyer(self.is_human)