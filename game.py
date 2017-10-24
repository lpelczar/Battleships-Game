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
        turn = 0
        while True:
            self.player1.player_turn()
            hit_position = self.get_user_input()
            hit_position = self.check_if_user_input_is_digit(hit_position[0], hit_position[1])
            print(hit_position)
            # metoda ktora sprawdza w co trafil player_name1, jesli tak petla bedzie sie powtarzac

            turn = 1
            while turn == 1:
                self.player2.player_turn()
                hit_position = self.get_user_input()
                hit_position = self.check_if_user_input_is_digit(hit_position[0], hit_position[1])
                # metoda ktora sprawdza w co trafil player_name1, jesli tak petla bedzie sie powtarzac

                turn = 0

    @staticmethod
    def check_if_user_input_is_digit(row, line):
        if not row.isdigit() or not len(row) == 1:
            print('You type wrong sign or number! Try again.')

        elif not line.isdigit() and not len(line) == 1:
            print('You type wrong sign or number! Try again.')

        else:
            row = int(row)
            line = int(line)
            print('Fire!')

        return (row, line)

    @staticmethod
    def get_user_input():
        hit_row = input('Enter number of row you want to hit: ')
        hit_line = input('Enter number of line you want to hit: ')
        hit_position = (hit_row, hit_line)

        return hit_position
