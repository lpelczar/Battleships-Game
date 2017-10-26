import os
from time import sleep

import game
from ship import *


class Player():
    """
    Class representing a player with his board and opponent board as attributes
    """
    def __init__(self, name, is_human, ocean, opponent_ocean):
        """
        :param name: String -> Name of the player
        :param is_human: bool -> True if Player is Human, else False
        :param ocean: Ocean -> player board
        :param opponent_ocean: Ocean -> Opponent ocean
        """
        self.name = name
        self.ocean = ocean
        self.opponent_ocean = opponent_ocean
        self.is_human = is_human
        self.name = name
        self.total_hits = 0
        self.misses = 0

    def put_ship_on_board(self, ship_name, is_horizontal, starting_point, is_decoy=False):
        """
        Create ship object and place it on board.

        :param ship_name: String -> Name of a ship
        :param is_horizontal: bool -> True if ship is placed horizontally else False
        :param starting_point: int, int -> Tuple with starting point of a ship (row, line)
        :param is_decoy: bool -> True if you are placing ship on additional temp board default: False
        """
        eval(ship_name)(self.is_human, self.ocean, is_horizontal, starting_point, is_decoy)

    def player_turn(self, player_name):
        """
        Print table with both boards for player turn

        :param player_name: String -> Name of a Player object
        """
        ocean_lines = self.ocean.__str__().split('\n')
        game.Game.hide_all_ships(self.opponent_ocean)
        ocean2_lines = self.opponent_ocean.__str__().split('\n')
        game.Game.show_all_ships(self.opponent_ocean)
        width = 45
        table_names = 'Your Ocean: ' + ' ' * width + 'Opponent Ocean:'

        print('Turn: ', player_name, '\n', table_names)
        for i in range(0, len(ocean_lines)):
            print(ocean_lines[i] + '     ' + ocean2_lines[i])

    def shot_outcome(self, positions):
        """
        Change the sign of a square to '0' if you miss or change the ShipSquare to OceanSquare if you hit.

        :param positions: int, int -> Tuple with shooted position
        """
        ROW_INDEX = 0
        LINE_INDEX = 1

        row = positions[ROW_INDEX]
        line = positions[LINE_INDEX]
        if not isinstance(self.opponent_ocean.board[line][row], ShipSquare):
            self.opponent_ocean.board[line][row].change_sign('0')
            self.misses += 1
            self.total_hits += 1
            print('Shot missed')
            return False
        else:
            self.opponent_ocean.board[line][row] = OceanSquare('X')
            self.total_hits += 1
            print('Hit!')
            return True

    def ai_find_and_shoot(self, player_ocean):
        for line in player_ocean.board:
            for square in line:
                if isinstance(square, ShipSquare):
                    line[line.index(square)] = OceanSquare('X')
                    print('Hit!')
                    print(player_ocean)
                    sleep(1)
                    os.system('clear')
                    return

    def ai_guess(self, difficulty_level, player_ocean, player):
        """
        Computer is shooting our ocean depending on the given difficulty level.

        :param difficulty_level: String -> Level 0: easy, 1: medium, 2: hard
        :param player_ocean: Ocean -> Players board
        :param player: Player -> Player object
        """
        print("Computer turn")
        player_ships_sign = ["BA", "CA", "CR", "SU", "DE"]

        MIN_ROW = 1
        MAX_ROW = 8
        MIN_HIT_CHANCE = 0
        MAX_HIT_CHANCE = 50
        MIN_VALUE_FOR_HIT = 40

        while True:
            hit_success = random.randint(MIN_HIT_CHANCE, MAX_HIT_CHANCE * int(difficulty_level))
            if hit_success > MIN_VALUE_FOR_HIT:
                self.ai_find_and_shoot(player_ocean)

            else:
                row = random.randint(MIN_ROW, MAX_ROW)
                line = random.randint(MIN_ROW, MAX_ROW)
                positions = [row, line]
                if not self.shot_outcome(positions):
                    break

            for sign in player_ships_sign:
                    if player.check_if_ship_is_destroyed(sign, player_ocean):
                        print("Your ship: " + sign + " has been sunk!")
                        player_ships_sign.remove(sign)

            if not player_ships_sign:
                    print("You lose FOOL!!!!!")
                    sleep(2)
                    return True
        os.system('clear')
        
    def __str__(self):
        return self.name
