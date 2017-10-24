from ocean import Ocean
import random

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

                    print(start_x, start_y)
                    for i in range (1, self.space+1):
                        self.ocean.ocean[start_x][start_y] = self.sign
                        start_y +=1 if orientatnion == 'horizontal' else 0
                        start_x += 1 if orientatnion == 'vertical' else 0
                break
            except:
                continue





    def __repr__(self):
        return self.sign


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


