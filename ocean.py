from texttable import Texttable
from square import *


class Ocean():
    """
    Class representing one board with list of lists attribute
    """
    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self, height=10, width=10):
        """
        Create board with list of lists containing Square objects.

        :param height: int -> Height of board, default: 10
        :param width: int -> Width of board, default: 10
        """
        if self.board:
            self.board = []
        for c in range(0, height):
            self.board.append([OceanSquare() for i in range(width)])

        for k, v in enumerate(self.board):
            if k == 0 or k == height-1:
                for c, x in enumerate(v):
                    v[c] = BorderSquare()
            else:
                for c, x in enumerate(v):
                    if c == 0 or c == width-1:
                        v[c] = BorderSquare()

    def put_all_ships_for_bot(self):
        """
        Create all different ships from computer
        """
        import ship
        ship.Carrier(False, self, None, None)
        ship.Battleship(False, self, None, None)
        ship.Cruiser(False, self, None, None)
        ship.Submarine(False, self, None, None)
        ship.Destroyer(False, self, None, None)

    def __str__(self):
        """
        Print board using textable module
        """
        FIRST_LINE_INDEX = 0

        column_names = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        row_names = ['A ', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        t = Texttable()
        t.add_row(column_names)
        for row in self.board:
            row.insert(FIRST_LINE_INDEX, row_names.pop(FIRST_LINE_INDEX))
            t.add_row(row)
            row.pop(FIRST_LINE_INDEX)
        return t.draw()
