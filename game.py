import abc
import os
from copy import deepcopy
from highscore import HighScoreManager
from keygetch import getch
from player import Player
from ship import *


class Game():

    def __init__(self):
        self.start_time = time()

    @abc.abstractmethod
    def start_game(self):
        pass

    @staticmethod
    def is_horizontal_input(ship_name):
        """
        Method checks in which orientation player is keen to place the ship.
        :param ship_name: str - > name of the ship
        :return: bool -> if horizontal returns
        """
        while True:
            user_input = input('Do you want your ' + ship_name + ' placed horizontal or vertical? (h or v) ').lower()
            if user_input == 'h':
                return True
            elif user_input == 'v':
                return False
            else:
                print('Wrong input!')

    @staticmethod
    def convert_user_input_to_coordinates(row, column):
        """
        Method converts user input to coordinates
        :param row: str - > row input
        :param column: str - > column input
        :return: None
        """
        board_letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
        row = int(row) - 1

        if column in board_letter:
            column = board_letter.get(column)

        return (row, column)

    @staticmethod
    def get_user_input():
        """
        Method gets user coordinates input
        :return: list -> a list containg input, where 0 index is row, and 1 index is column
        """
        while True:
            hit_position = input('Enter coordinates you want to shoot (column,row): ')
            try:
                row, column = hit_position.split(',')
            except:
                print('Your type is wrong, try again!')
                continue

            column = column.upper()

            if not row.isdigit() or not len(row) == 1 or row == 0:
                print('You type wrong sign or number! Try again.')
                continue

            if not column.isalpha() or not len(column) == 1:
                print('You type wrong sign or number! Try again.')
                continue

            hit_position = (row, column)

            return hit_position

    @staticmethod
    def check_if_ship_is_destroyed(ship_sign: str, Ocean):
        """
        Method check if certain ships is destroyed.
        :param ship_sign: two char sign of ship i.e. "CA"
        :param Ocean: ocean object
        :return: bool - > False if ship is not destroyed, otherwise True
        """
        board = Ocean.board
        for row in board:
            for square in row:
                if square.sign == ship_sign.upper():
                    return False
        return True

    @staticmethod
    def check_if_all_ship_are_destroyed(ocean:Ocean):
        """
        Method check if certain ships is destroyed.
        :param Ocean: ocean object
        :return: bool - > False if all ships are not destroyed, otherwise True
        """
        board = Ocean.board
        for row in board:
            for square in row:
                if isinstance(square, OceanSquare):
                    return False
        return True

    def put_ships_on_board(self, player):
        """
        Method put all ships on board
        :param player: Player -> player instance
        :return:
        """
        ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
        movement_keys = ['w', 's', 'a', 'd']
        decoy_ocean = Ocean()
        decoy = Player('decoy', False, decoy_ocean, player.ocean)

        print('Creating mode:\n' + str(player) + "'s board")
        print(decoy.ocean)

        while ships:
            starting_position = 1, 1
            is_horizontal = self.is_horizontal_input(ships[0])

            while True:
                decoy.ocean.board = deepcopy(player.ocean.board)
                os.system('clear')
                decoy.put_ship_on_board(ships[0], is_horizontal, starting_position, True)
                print('Creating mode:\n' + str(player) + "'s board")
                print(decoy.ocean)

                print('use w,s,a,d to move your ship, than p to place it. You can restart placing with r and'
                      ' quit with q ')

                move_ship = getch()
                if move_ship in movement_keys:
                    starting_position = self.move_ship_on_board(is_horizontal, starting_position, ships[0], move_ship)

                elif move_ship == 'p':
                    try:
                        player.put_ship_on_board(ships[0], is_horizontal, starting_position, False)
                        ships.pop(0)
                        break
                    except:
                        print('You cant place ship here!')
                        continue

                elif move_ship =='q':
                    quit()

                elif move_ship == 'r':
                    player.ocean = Ocean()
                    os.system('clear')
                    self.put_ships_on_board(player)

                else:
                    print('Incorrect input!')

    @staticmethod
    def move_ship_on_board(is_horizontal, position, ship_type, move_ship):
        """
        Method puts ships on board using WSAD buttons
        :param is_horizontal: bool - > is ship orientation horizontal
        :param position: list -> list containing starting postition
        :param ship_type: str -> ship type
        :param move_ship: str -> direction
        :return: None
        """
        position = list(position)
        ships_lengths = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        ship_length = ships_lengths[ship_type]
        if is_horizontal:
            if move_ship == 'w':
                if position[1] > 1:
                    position[1] -= 1

            elif move_ship == 's':
                if position[1] < 8:
                    position[1] += 1

            elif move_ship == 'a':
                if position[0] > 1:
                    position[0] -= 1

            elif move_ship == 'd':
                if position[0] < 9 - ship_length:
                    position[0] += 1
        else:
            if move_ship == 'w':
                if position[1] > 1:
                    position[1] -= 1

            elif move_ship == 's':
                if position[1] < 9 - ship_length:
                    position[1] += 1

            elif move_ship == 'a':
                if position[0] > 1:
                    position[0] -= 1

            elif move_ship == 'd':
                if position[0] < 8:
                    position[0] += 1

        position = tuple(position)

        return position

    @staticmethod
    def get_position_input(ship_name):
        """
        Method get from user starting ship position and return coordinates
        :param ship_name: str-> name of the ship
        :return: int, int - > coordinates
        """
        while True:
            position = input('Enter starting position of a ' + ship_name + ': (x,y) ')
            board_letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
            try:
                x, y = position.split(',')
                x = int(x) - 1
                if y.isalpha():
                    y = y.upper()
                    if y in board_letter:
                        y = board_letter.get(y)
                else:
                    y = int(y) - 1
                break
            except:
                print('Wrong input!')
                continue
        return x, y

    @staticmethod
    def hide_all_ships(Ocean):
        """
        Method hide all ships from ocean board
        :param Ocean:
        :return: None
        """
        board = Ocean.board
        for row in board:
            for square in row:
                if isinstance(square, ShipSquare):
                    square.change_sign(' ')

    @staticmethod
    def show_all_ships(Ocean):
        """
        Method all hidden from ocean board
        :param Ocean:
        :return: None
        """
        board = Ocean.board
        for row in board:
            for square in row:
                if isinstance(square, ShipSquare):
                    square.change_sign(square.final_sign)


class SingleGame(Game):

    def __init__(self, player_name, difficulty_level):
        self.difficulty_level = difficulty_level  #difficulty level where 0 = easy, 1 = medium, 2 = hard
        self.ocean_player_1 = Ocean()
        self.ocean_bot = Ocean()
        self.player = Player(player_name, True, self.ocean_player_1, self.ocean_bot)
        self.bot = Player('Computer', False, self.ocean_bot, self.ocean_player_1)
        self.ship_signs = ["BA", "CA", "CR", "SU", "DE"]

    def start_game(self):
        self.ocean_bot.put_all_ships_for_bot()
        self.put_ships_on_board(self.player)

        os.system('clear')
        while True:
            self.player.player_turn(self.player.name)
            hit_position = self.get_user_input()
            hit_position = self.convert_user_input_to_coordinates(hit_position[0], hit_position[1])
            os.system('clear')
            shot_outcome = self.player.shot_outcome(hit_position)

            for sign in self.ship_signs:

                if self.check_if_ship_is_destroyed(sign, self.ocean_bot):
                    self.ship_signs.remove(sign)
                    print("Enemy ship: " + sign + " has been sunk!")

            if not self.ship_signs:
                win = self.player1.name, 'win game! Congratulations!'
                print(win)
                end_time = time()
                end_time = int(end_time - start_time)
                HighScoreManager().add_to_highscore(self.player1.name, self.player1.total_hits, self.player1.misses, end_time)
                return win

            if shot_outcome:
                continue

            bot_turn = self.bot.ai_guess(self.difficulty_level, self.ocean_player_1, self)
            if bot_turn:
                break


class MultiPlayerGame(Game):

    def __init__(self, player_name_1, player_name_2):
        self.ocean_player_1 = Ocean()
        self.ocean_player_2 = Ocean()
        self.player1 = Player(player_name_1, True, self.ocean_player_1, self.ocean_player_2)
        self.player2 = Player(player_name_2, True, self.ocean_player_2, self.ocean_player_1)

    def start_game(self):
        turn = 0
        self.put_ships_on_board(self.player1)
        os.system('clear')
        self.put_ships_on_board(self.player2)
        os.system('clear')

        while True:
            self.player1.player_turn(self.player1.name)

            incorrect_inputs = False
            while incorrect_inputs is False:
                hit_position = self.get_user_input()
                hit_position = self.convert_user_input_to_coordinates(hit_position[0], hit_position[1])

            is_hit = self.player1.shot_outcome(hit_position)
            is_win = self.check_if_all_ship_are_destroyed(self.ocean_player_2)

            if is_win is True:
                win = self.player1.name, 'win game! Congratulations!'
                print(win)
                end_time = time()
                end_time = int(end_time - start_time)
                HighScoreManager().add_to_highscore(self.player1.name, self.player1.total_hits, self.player1.misses, end_time)

                return win

            if is_hit is True:
                continue

            turn = 1
            while turn == 1:
                self.player2.player_turn(self.player2.name)

                incorrect_inputs = False
                while incorrect_inputs is False:
                    hit_position = self.get_user_input()
                    incorrect_inputs = self.check_if_user_input_is_correct(hit_position[0], hit_position[1])
                    hit_position = self.convert_user_input_to_coordinates(hit_position[0], hit_position[1])

                is_hit = self.player2.shot_outcome(hit_position)
                is_win = self.check_if_all_ship_are_destroyed(self.ocean_player_1)

                if is_win is True:
                    win = self.player2.name, 'win game! Congratulations!'
                    print(win)
                    end_time = time()
                    end_time = int(end_time - start_time)
                    HighScoreManager().add_to_highscore(self.player2.name, self.player2.total_hits, self.player2.misses, end_time)
                    return win

                if is_hit is True:
                    turn = 1
                else:
                    turn = 0
