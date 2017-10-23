from time import time

class Player():

    def __init__(self, name:str, is_human:bool, ocean:Ocean):
        self.name = name
        self.start_time = time()

    def add_ship_to_ocean(self):
        ca = Carrier(self.is_human)
        ba = BattleShip(self.is_human)
        cr = Cruiser(self.is_human)
        su = Submarine(self.is_human)
        de = Destroyer(self.is_human)



class Ocean():

    def __init__(self):
        self.ocean = []
        self.create_board()

    def create_board(self, height=10, width=10):
        for c in range(0, height):
            self.ocean.append([OceanSquare() for i in range(width)])

        for k,v in enumerate(self.ocean):
            if k == 0 or k == height-1:
                for c,x in enumerate(v):
                    v[c] = BorderSquare()
            else:
                for c,x in enumerate(v):
                    if c == 0 or c == width-1:
                        v[c] = BorderSquare()

    def __str__(self):
        return "\n".join([str(i) for i in self.ocean])




class Square:

    def __init__(self, sign):
        self.sign = sign

    def change_sign(self, sign):
        self. sign = sign

    def __repr__(self):
        return self.sign



class BorderSquare(Square):

    def __init__(self):
        super().__init__("~")


class OceanSquare(Square):


    def __init__(self, ShipReference= None):
        if(ShipReference == None):
            super().__init__(" ")
        else:
            super().__init__(ShipReference)




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


ocean = Ocean()
print(ocean)
