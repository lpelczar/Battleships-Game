import abc
from ocean import Ocean
from player import Player

@abc.abstractproperty
class Game():

    def __init__(self):
        ...

    @abc.abstractmethod
    def start_game(self):
        ...


class SingleGame(Game):

    def __init__(self, player_name:str, difficulty_level:int):
        self.difficulty_level = difficulty_level #difficulty level where 0 = easy, 1 = medium, 2 = hard
        self.player_name
        player_ocean = Ocean()
        human_player = Player(player_name, True , player_ocean)
        bot_ocean = Ocean()
        bot_player = Player('Bot',False, bot_ocean)


    def start_game(self):
        ...

class MultiPlayerGame(Game):

    def __init__(self, player_name:str):
        ...

    def start_game(self):
        ...
