import abc
import os
from ocean import Ocean
from player import Player


class Game():

    def __init__(self):
        pass

    @abc.abstractmethod
    def start_game(self):
        pass

    def put_ships_on_board(self, player):
        ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']

        while ships:
            os.system('clear')
            print(player)
            print(player.ocean)
            is_horizontal = self.is_horizontal_input(ships[0])
            starting_position = self.get_position_input(ships[0])
            try:
                player.put_ship_on_board(ships[0], is_horizontal, starting_position)
            except:
                print('You cant place ship here!')
                continue
            ships.pop(0)

    @staticmethod
    def get_position_input(ship_name):
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
    def is_horizontal_input(ship_name):
        while True:
            user_input = input('Do you want your ' + ship_name + ' placed horizontal or vertical? (h or v) ').lower()
            if user_input == 'h':
                return True
            elif user_input == 'v':
                return False
            else:
                print('Wrong input!')

    @staticmethod
    def check_if_user_input_is_correct(row, line):

        if not row.isdigit() or not len(row) == 1:
            print('You type wrong sign or number! Try again.')
            return False

        if not line.isalpha() or not len(line) == 1:
            print('You type wrong sign or number! Try again.')
            return False

        else:
            return True

    @staticmethod
    def convert_user_input_to_coordinates(row, line):
        try:
            board_letter = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 7}
            row = int(row) - 1

            if line in board_letter:
                line = board_letter.get(line)
        except:
            print('Wring sings!')

        return (row, line)

    @staticmethod
    def get_user_input():
        hit_row = input('Enter number of row you want to hit: ')
        hit_line = input('Enter number of line you want to hit: ').upper()
        hit_position = (hit_row, hit_line)

        return hit_position

    @staticmethod
    def check_if_ship_is_destroyed(ship_sign: str, Ocean):
        board = Ocean.board
        for row in board:
            for square in row:
                if square.sign == ship_sign.upper():
                    return False
        return True


class SingleGame(Game):

    def __init__(self, player_name, difficulty_level):
        self.difficulty_level = difficulty_level #difficulty level where 0 = easy, 1 = medium, 2 = hard
        self.ocean_player_1 = Ocean()
        self.ocean_bot = Ocean()
        self.player = Player(player_name, True, self.ocean_player_1, self.ocean_bot)
        self.bot = Player('Computer', False, self.ocean_bot, self.ocean_player_1)

    def start_game(self):
        self.ocean_bot.put_all_ships_for_bot()
        print(self.ocean_bot)
        turn = 0
        while True:
            self.player.player_turn()
            hit_position = self.get_user_input()
            incorrect_inputs = self.check_if_user_input_is_correct(hit_position[0], hit_position[1])
            hit_position = self.convert_user_input_to_coordinates(hit_position[0], hit_position[1])
            print(hit_position)
            self.player.shot_outcome(hit_position)

            turn = 1

            self.bot.player_turn()

                # AI strzela rozpierdziela!


class MultiPlayerGame(Game):

    def __init__(self, player_name_1, player_name_2):
        self.ocean_player_1 = Ocean()
        self.ocean_player_2 = Ocean()
        self.player1 = Player(player_name_1, True, self.ocean_player_1, self.ocean_player_2)
        self.player2 = Player(player_name_2, True, self.ocean_player_2, self.ocean_player_1)

    def start_game(self):
        turn = 0
        self.put_ships_on_board(self.player1)
        self.put_ships_on_board(self.player2)

        while True:
            self.player1.player_turn()

            incorrect_inputs = False
            while incorrect_inputs is False:  # kontola inputow
                hit_position = self.get_user_input()
                incorrect_inputs = self.check_if_user_input_is_correct(hit_position[0], hit_position[1])
                hit_position = self.convert_user_input_to_coordinates(hit_position[0], hit_position[1])

            print(hit_position)
            self.player1.shot_outcome(hit_position)
            # metoda ktora sprawdza w co trafil player_name1, jesli tak petla bedzie sie powtarzac

            turn = 1
            while turn == 1:
                self.player2.player_turn()

                incorrect_inputs = False
                while incorrect_inputs is False:  # kontola inputow
                    hit_position = self.get_user_input()
                    incorrect_inputs = self.check_if_user_input_is_correct(hit_position[0], hit_position[1])
                    hit_position = self.convert_user_input_to_coordinates(hit_position[0], hit_position[1])

                self.player2.shot_outcome(hit_position)
                # metoda ktora sprawdza w co trafil player_name1, jesli tak petla bedzie sie powtarzac

                turn = 0
