class Square:
    """
    Class for representation of a single Square on board
    """
    def __init__(self, sign):
        """
        :param sign: str -> String representation of square
        """
        self.sign = sign
        self.final_sign = sign

    def change_sign(self, sign):
        """
        Change the sign of a Square object

        :param sign: str -> String representation of square
        """
        self.sign = sign

    def __repr__(self):
        """
        Return string representation of a Square
        """
        return self.sign

    def __str__(self):
        """
        Return string representation of a Square
        """
        return self.sign


class BorderSquare(Square):
    """
    Concrete class representing the Border
    """
    def __init__(self):
        super().__init__("~")


class OceanSquare(Square):
    """
    Concrete class representing the playable Ocean
    """
    def __init__(self, ShipReference=None):
        """
        :param ShipReference: str -> String representation of OceanSquare
        """
        if(ShipReference is None):
            super().__init__(" ")
        else:
            super().__init__(ShipReference)


class ShipSquare(Square):
    """
    Concrete class representing the Ship
    """
    def __init__(self, sign):
        """
        :param sign: str -> String representation of square
        """
        super().__init__(sign)
