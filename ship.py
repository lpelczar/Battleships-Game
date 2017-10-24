from ocean import Ocean
from square import ShipSquare
from square import *
import random
import traceback


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

        if x < 1 or y < 1 or x + self.space > 9 or y + self.space > 9:
            raise ValueError('Your ship is hanging off the border!')

        if self.is_another_ship_near(x, y):
            raise ValueError('You cant put ship near another ship!')

        if self.is_horizontal:
            self.ocean.ocean[y][x: x + self.space] = [ShipSquare(self.sign) for i in range(self.space)]
        else:
            for i in self.ocean.ocean[y:y + self.space]:
                i[x] = ShipSquare(self.sign)

    def is_another_ship_near(self, x, y):
        surrounding = []

        if self.is_horizontal:
            surrounding += self.ocean.ocean[y + 1][x - 1: x + 1 + self.space]
            surrounding += self.ocean.ocean[y][x - 1: x + 1 + self.space]
            surrounding += self.ocean.ocean[y - 1][x - 1: x + 1 + self.space]
        else:
            surrounding += [i[x - 1] for i in self.ocean.ocean[y - 1: y + 1 + self.space]]
            surrounding += [i[x] for i in self.ocean.ocean[y - 1: y + 1 + self.space]]
            surrounding += [i[x + 1] for i in self.ocean.ocean[y - 1: y + 1 + self.space]]
        return any(isinstance(i, ShipSquare) for i in surrounding)

    def create_ship_by_computer(self):
        while True:
            try:
                orientatnion = random.choice(['horizontal', 'vertical'])
                start_x = 0
                start_y = 0
                position_found = False
                self.is_horizontal = True if orientatnion == 'horizontal' else False
                while not position_found:
                    start_x = random.choice(range(1, 9))
                    start_y = random.choice(range(1, 9))
                    if self.is_another_ship_near(start_y, start_x):
                        continue
                    temp_start_x = start_x
                    temp_start_y = start_y
                    try:
                        for i in range(1, self.space + 1):
                            square_sign = self.ocean.ocean[temp_start_x][temp_start_y].sign
                            if not square_sign == ' ':
                                position_found = False
                                break
                            temp_start_y += 1 if orientatnion == 'horizontal' else 0
                            temp_start_x += 1 if orientatnion == 'vertical' else 0
                            position_found = True
                    except IndexError:
                        traceback.print_exc()
                        continue

                for i in range (1, self.space+1):
                    self.ocean.ocean[start_x][start_y] = ShipSquare(self.sign)
                    start_y +=1 if orientatnion == 'horizontal' else 0
                    start_x += 1 if orientatnion == 'vertical' else 0
                break
            except:
                continue


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
