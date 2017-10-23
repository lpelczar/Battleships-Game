class Ocean():
    ...

    def create_board(width, height):
        board = []
        for c in range(0, height):
            board.append([' '] * width)

        for k,v in enumerate(board):
            if k == 0 or k == height-1:
                for c,x in enumerate(v):
                    v[c] = 'X'
            else:
                for c,x in enumerate(v):
                    if c == 0 or c == width-1:
                        v[c] = 'X'
        print(board)
        return board




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
