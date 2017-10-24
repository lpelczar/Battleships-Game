import abc
from ocean import Ocean
from player import Player


class Game():

    # def __init__(self):
    #     pass

    @abc.abstractmethod
    def start_game(self):
        pass


class SingleGame(Game):

    def __init__(self, player_name:str, difficulty_level:int):
        self.difficulty_level = difficulty_level #difficulty level where 0 = easy, 1 = medium, 2 = hard
        self.player_name
        player_ocean = Ocean()
        human_player = Player(player_name, True ,player_ocean)
        bot_ocean = Ocean()
        bot_player = Player('Bot', False, bot_ocean)


    def start_game(self):
        ...


class MultiPlayerGame(Game):

    def __init__(self, player_name_1, player_name_2):
        self.ocean_player_1 = Ocean()
        self.ocean_player_2 = Ocean()
        self.player1 = Player(player_name_1, True, self.ocean_player_1)
        self.player2 = Player(player_name_2, True, self.ocean_player_2)

    def start_game(self):
        while True:
            self.player1.player_turn()
            hit_row = input('Enter number of row you want to hit: ')
            hit_line = input('Enter number of line you want to hit: ')
            hit_position = (hit_row, hit_line)
            check_if_user_input_is_digit(hit_row, line)

    @staticmethod
    def check_if_user_input_is_digit(row, line):
        if row.isdigit():
            row = int(row)

        elif line.isdigit():
            line = int(line)

        else:
            print('You didnt type a number! Try again')

        return (row, line)
