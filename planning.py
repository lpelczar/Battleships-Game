class Ocean():
    ...




class Square:

    def __init__(self, sign):
        self.sign = sign

    def change_sign(self, sign):
        self. sign = sign



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
    def __init__(self, space:int, sign:str, player_create:bool):
        self.space = space
        self.sign = sign
        if player_create:
            self.create_ship_by_user()
        else:
            self.create_ship_by_computer()


    def create_ship_by_user(self):
        ...

    def create_ship_by_computer(self):
        ...


class Carrier(Ship):

    def __init__(self):
        super().__init__(5, "CR")
