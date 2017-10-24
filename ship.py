from ocean import Ocean


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
        ...


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
