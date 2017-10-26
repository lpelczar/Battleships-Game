import random

from ocean import Ocean
from square import *
from time import time

ROW_INDEX = 0
LINE_INDEX = 1


class Ship():
    """
    Class representing Ship object on board
    """
    def __init__(self, space: int, sign: str, player_create: bool, ocean: Ocean,
                 is_horizontal: bool, starting_point: (int, int), is_decoy=False):
        """
        :param space: int -> Length of a ship
        :param sign: str -> String representation of a ship
        :param player_create: bool -> True if player is creating ship, False if computer is creating ship
        :param ocean: Ocean -> Ocean where the ship is placed
        :param is_horizontal: bool -> True if ship is placed horizontal, False if it is placed vertical
        :param starting_point: int, int -> Tuple with starting point of a ship (row, line)
        :param is_decoy: bool -> True if you are placing ship on additional temp board default: False
        """
        self.space = space
        self.sign = sign
        self.ocean = ocean
        self.is_horizontal = is_horizontal
        if player_create:
            self.create_ship_by_user(starting_point)
        elif is_decoy:
            self.create_ship_by_decoy(starting_point)
        else:
            self.create_ship_by_computer()

    def create_ship_by_user(self, starting_point):
        """
        Check if ship can be placed here and add ship on board:

        The ships can only be placed vertically or horizontally.
        Diagonal placement is not allowed.
        No part of a ship may hang off the edge of the board.
        Ships may not overlap each other.
        No ships may be placed on another ship. Ships may not touch each other.

        :param starting_point: int, int -> Tuple with starting point of a ship (row, line)
        """
        MIN_INDEX = 0
        MAX_INDEX = 9

        x = starting_point[ROW_INDEX]
        y = starting_point[LINE_INDEX]

        if self.is_horizontal:
            if x <= MIN_INDEX or x + self.space > MAX_INDEX or y <= MIN_INDEX or y >= MAX_INDEX:
                raise ValueError('Your ship is hanging off the border!')
        else:
            if y <= MIN_INDEX or y + self.space > MAX_INDEX or x <= MIN_INDEX or x >= MAX_INDEX:
                raise ValueError('Your ship is hanging off the border!')

        if self.is_another_ship_near(x, y):
            raise ValueError('You cant put ship near another ship!')

        if self.is_horizontal:
            self.ocean.board[y][x: x + self.space] = [ShipSquare(self.sign) for i in range(self.space)]
        else:
            for i in self.ocean.board[y:y + self.space]:
                i[x] = ShipSquare(self.sign)

    def create_ship_by_decoy(self, position):
        """
        Used for moving ship while placing it, to do it we create temporary additional ocean

        :param position: int, int -> Tuple with starting point of a ship (row, line)
        """
        x = position[ROW_INDEX]
        y = position[LINE_INDEX]
        if self.is_horizontal:
            self.ocean.board[y][x: x + self.space] = [ShipSquare(self.sign) for i in range(self.space)]
        else:
            for i in self.ocean.board[y:y + self.space]:
                i[x] = ShipSquare(self.sign)

    def is_another_ship_near(self, x, y):
        """
        Chceck if there is another ship around ship with given position

        :param x: int -> Row
        :param y: int -> Line
        """
        BUFFER = 1

        surrounding = []

        if self.is_horizontal:
            surrounding += self.ocean.board[y + BUFFER][x - BUFFER: x + BUFFER + self.space]
            surrounding += self.ocean.board[y][x - BUFFER: x + BUFFER + self.space]
            surrounding += self.ocean.board[y - BUFFER][x - BUFFER: x + BUFFER + self.space]
        else:
            surrounding += [i[x - BUFFER] for i in self.ocean.board[y - BUFFER: y + BUFFER + self.space]]
            surrounding += [i[x] for i in self.ocean.board[y - BUFFER: y + BUFFER + self.space]]
            surrounding += [i[x + BUFFER] for i in self.ocean.board[y - BUFFER: y + BUFFER + self.space]]
        return any(isinstance(i, ShipSquare) for i in surrounding)

    def create_ship_by_computer(self):
        """
        Place randomly all ships on the board.
        """
        MIN_BOARD_INDEX = 1
        MAX_BOARD_INDEX = 9

        MULTIPLIER = 1000.0  # Convert time to miliseconds
        MAX_DIFF = 500

        start = time()
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            self.is_horizontal = True if orientation == 'horizontal' else False
            x = random.choice(range(MIN_BOARD_INDEX, MAX_BOARD_INDEX))
            y = random.choice(range(MIN_BOARD_INDEX, MAX_BOARD_INDEX))
            try:
                self.create_ship_by_user([y, x])
            except:
                end = time()
                diff = int((end-start) * MULTIPLIER)
                if diff > MAX_DIFF:
                    self.ocean.create_board()
                    self.ocean.put_all_ships_for_bot()
                continue
            break

    def __str__(self):
        return self.sign


class Carrier(Ship):

    def __init__(self, player_create: bool, ocean: Ocean,
                 is_horizontal: bool, starting_point: (int, int), is_decoy=False):
        super().__init__(5, "CA", player_create, ocean, is_horizontal, starting_point, is_decoy)


class Battleship(Ship):

    def __init__(self, player_create: bool, ocean: Ocean,
                 is_horizontal: bool, starting_point: (int, int), is_decoy=False):
        super().__init__(4, "BA", player_create, ocean, is_horizontal, starting_point, is_decoy)


class Cruiser(Ship):

    def __init__(self, player_create: bool, ocean: Ocean,
                 is_horizontal: bool, starting_point: (int, int), is_decoy=False):
        super().__init__(3, "CR", player_create, ocean, is_horizontal, starting_point, is_decoy)


class Submarine(Ship):

    def __init__(self, player_create: bool, ocean: Ocean,
                 is_horizontal: bool, starting_point: (int, int), is_decoy=False):
        super().__init__(3, "SU", player_create, ocean, is_horizontal, starting_point, is_decoy)


class Destroyer(Ship):
    def __init__(self, player_create: bool, ocean: Ocean,
                 is_horizontal: bool, starting_point: (int, int), is_decoy=False):
        super().__init__(2, "DE", player_create, ocean, is_horizontal, starting_point, is_decoy)
