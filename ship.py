import random

from ocean import Ocean
from square import *
from time import time


class Ship():

    def __init__(self, space: int, sign: str, player_create: bool, ocean: Ocean, is_horizontal: bool, starting_point: (int, int)):
        self.space = space
        self.sign = sign
        self.ocean = ocean
        self.is_horizontal = is_horizontal
        if player_create:
            self.create_ship_by_user(starting_point)
        else:
            self.create_ship_by_computer()

    def create_ship_by_user(self, starting_point):
        x = starting_point[0]
        y = starting_point[1]

        if self.is_horizontal:
            if x <= 0 or x + self.space >= 9 or y <= 0 or y >= 9:
                raise ValueError('Your ship is hanging off the border!')
        else:
            if y <= 0 or y + self.space >= 9 or x <= 0 or x >= 9:
                raise ValueError('Your ship is hanging off the border!')

        if self.is_another_ship_near(x, y):
            raise ValueError('You cant put ship near another ship!')

        if self.is_horizontal:
            self.ocean.board[y][x: x + self.space] = [ShipSquare(self.sign) for i in range(self.space)]
        else:
            for i in self.ocean.board[y:y + self.space]:
                i[x] = ShipSquare(self.sign)

    def is_another_ship_near(self, x, y):
        surrounding = []

        if self.is_horizontal:
            surrounding += self.ocean.board[y + 1][x - 1: x + 1 + self.space]
            surrounding += self.ocean.board[y][x - 1: x + 1 + self.space]
            surrounding += self.ocean.board[y - 1][x - 1: x + 1 + self.space]
        else:
            surrounding += [i[x - 1] for i in self.ocean.board[y - 1: y + 1 + self.space]]
            surrounding += [i[x] for i in self.ocean.board[y - 1: y + 1 + self.space]]
            surrounding += [i[x + 1] for i in self.ocean.board[y - 1: y + 1 + self.space]]
        return any(isinstance(i, ShipSquare) for i in surrounding)

    def create_ship_by_computer(self):
        start = time()
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            self.is_horizontal = True if orientation == 'horizontal' else False
            x = random.choice(range(1, 9))
            y = random.choice(range(1, 9))
            try:
                self.create_ship_by_user([y, x])
            except:
                end = time()
                diff = int((end-start)*1000.0)
                if diff > 500:
                    self.ocean.create_board()
                    self.ocean.put_all_ships_for_bot()
                continue
            break

    def __str__(self):
        return self.sign


class Carrier(Ship):

    def __init__(self, player_create: bool, ocean: Ocean, is_horizontal: bool, starting_point: (int, int)):
        super().__init__(5, "CA", player_create, ocean, is_horizontal, starting_point)


class Battleship(Ship):

    def __init__(self, player_create: bool, ocean: Ocean, is_horizontal: bool, starting_point: (int, int)):
        super().__init__(4, "BA", player_create, ocean, is_horizontal, starting_point)


class Cruiser(Ship):

    def __init__(self, player_create: bool, ocean: Ocean, is_horizontal: bool, starting_point: (int, int)):
        super().__init__(3, "CR", player_create, ocean, is_horizontal, starting_point)


class Submarine(Ship):

    def __init__(self, player_create: bool, ocean: Ocean, is_horizontal: bool, starting_point: (int, int)):
        super().__init__(3, "SU", player_create, ocean, is_horizontal, starting_point)


class Destroyer(Ship):
    def __init__(self, player_create: bool, ocean: Ocean, is_horizontal: bool, starting_point: (int, int)):
        super().__init__(2, "DE", player_create, ocean, is_horizontal, starting_point)
