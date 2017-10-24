from time import time
from ship import *

class Player():

    def __init__(self, name, is_human, ocean):
        self.name = name
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

    def player_turn(self):
        print('Turn: ', self.name)
        print(self.ocean)

    def shot_outcome(self, ocean, positions):
        positions[0] = shot_position_x
        positions[1] = shot_position_y
        if not isinstace(ocean[shot_position_x, shot_position_y], ShipSquare):
            print('Shot missed')
            return False
        else:
            ocean[shot_position_x, shot_position_y].change_sign('X')
            print('Hit!')
            return True

    def ai_guess(self, difficulty_level, player_ocean):
        while True:
            hit_success = randint(0, 50 * difficulty_level)
            if hit_success > 30:
                for line in player_ocean:
                    for square in line:
                        if isinstance(square, ShipSquare):
                            print('Shot at: ' + str(player_ocean.index(square)) + str(line.index(square)) + 'outcome: ')
                            square.change_sign('X')
                            print('Hit!')
            else:
                shot_position_x = randint(1, 8)
                shot_position_y = randint(1, 8)
                positions = [shot_position_x, shot_position_y]
                print('Shot at: ' + str(shot_position_x) + str(shot_position_y) + 'outcome: ')
                if not self.shot_outcome(player_ocean, positions):
                    break
