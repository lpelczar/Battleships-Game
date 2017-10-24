from ocean import Ocean

class Ship():

    def __init__(self, space:int, sign:str, player_create:bool, ocean:Ocean):
        self.space = space
        self.sign = sign
        self.ocean = ocean
        if player_create:
            self.create_ship_by_user()
        else:
            self.create_ship_by_computer()


    def create_ship_by_user(self):
        ...

    def create_ship_by_computer(self):
        ...


class Carrier(Ship):

    def __init__(self, player_create:bool, ocean:Ocean):
        super().__init__(5, "CA", player_create, ocean)

class BattleShip(Ship):

    def __init__(self, player_create:bool, ocean:Ocean):
        super().__init__(4, "BA", player_create, ocean)

class Cruiser(Ship):

    def __init__(self, player_create:bool, ocean:Ocean):
        super().__init__(3, "CR", player_create, ocean)

class Submarine(Ship):

    def __init__(self, player_create:bool, ocean:Ocean):
        super().__init__(3, "SU", player_create, ocean)

class Destroyer(Ship):
    def __init__(self, player_create:bool, ocean:Ocean):
        super().__init__(2, "DE", player_create, ocean)