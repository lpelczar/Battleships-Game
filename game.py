import abc
from planning import *

@abc.abstractproperty
class Game():

    def __init__(self):
        ...

    @abc.abstractmethod
    def start_game(self):


class SingleGame(Game):

    def __init__(self, player_name:str):
        self.player_name
        first_ocean = Ocean()
        human_player = Player(player_name)


    def start_game(self):

