from ocean import Ocean
from square import *
import random


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
            raise ValueError('Wrong coords!')

        if self.is_horizontal:
            self.ocean.ocean[y][x: x + self.space] = [self.sign for i in range(self.space)]
        else:
            for i in self.ocean.ocean[y:y + self.space]:
                i[x] = self.sign

    def create_ship_by_computer(self):
        while True:
            try:
                orientatnion = random.choice(['horizontal', 'vertical'])
                start_x = 0
                start_y = 0
                y_position_found = False
                while not y_position_found:
                    start_x = random.choice(range(1, 9))
                    start_y = random.choice(range(1, 9))
                    temp_start_x = start_x
                    temp_start_y = start_y
                    try:
                        for i in range(1, self.space + 1):
                            square_sign = self.ocean.ocean[temp_start_x][temp_start_y].sign
                            if not square_sign == ' ':
                                y_position_found = False
                                break
                            temp_start_y += 1 if orientatnion == 'horizontal' else 0
                            temp_start_x += 1 if orientatnion == 'vertical' else 0
                            y_position_found = True
                    except:
                        continue
                for i in range (1, self.space+1):
                    self.ocean.ocean[start_x][start_y] = OceanSquare(self)
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


class BattleShip(Ship):

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