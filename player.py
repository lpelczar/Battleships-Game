from time import time
from ship import *
import random

class Player():

    def __init__(self, name, is_human, ocean, opponent_ocean):
        self.name = name
        self.ocean = ocean
        self.opponent_ocean = opponent_ocean
        self.is_human = is_human
        self.name = name
        self.start_time = time()

    def put_ship_on_board(self, ship_name, is_horizontal, starting_point):
        eval(ship_name)(self.is_human, self.ocean, is_horizontal, starting_point)

    def put_all_ships(self):
        Carrier(self.is_human, self.ocean, None, None)
        Battleship(self.is_human, self.ocean, None, None)
        Cruiser(self.is_human, self.ocean, None, None)
        Submarine(self.is_human, self.ocean, None, None)
        Destroyer(self.is_human, self.ocean, None, None)

    def player_turn(self):
        print('Turn: ', self.name)
        print(self.ocean)

    def shot_outcome(self, ocean, positions):
        shot_position_x = positions[0]
        shot_position_y = positions[1]
        if not isinstance(ocean.board[shot_position_x][shot_position_y], ShipSquare):
            print('Shot missed')
            return False
        else:
            ocean.board[shot_position_x][shot_position_y].change_sign('X')
            print('Hit!')
            return True

    def ai_guess(self, difficulty_level, player_ocean):
        while True:
            hit_success = random.randint(0, 50 * difficulty_level)
            if hit_success > 30:
                for line in player_ocean:
                    for square in line:
                        if isinstance(square, ShipSquare):
                            print('Shot at: ' + str(player_ocean.index(square)) + str(line.index(square)) + 'outcome: ')
                            square.change_sign('X')
                            print('Hit!')
                            print(player_ocean)
            else:
                shot_position_x = random.randint(1, 8)
                shot_position_y = random.randint(1, 8)
                positions = [shot_position_x, shot_position_y]
                print('Shot at: ' + str(shot_position_x) + str(shot_position_y) + 'outcome: ')
                print(player_ocean)
                if not self.shot_outcome(player_ocean, positions):
                    break
