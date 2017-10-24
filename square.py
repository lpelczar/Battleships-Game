class Square:

    def __init__(self, sign):
        self.sign = sign

    def change_sign(self, sign):
        self.sign = sign

    def __repr__(self):
        return self.sign


class BorderSquare(Square):
    def __init__(self):
        super().__init__("~")


class OceanSquare(Square):

    def __init__(self, ShipReference=None):
        if(ShipReference is None):
            super().__init__(" ")
        else:
            super().__init__(ShipReference)


class ShipSquare(Square):

    def __init__(self, sign):
        super().__init__(sign)
