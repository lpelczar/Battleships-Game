from ship import *
import random


class Player():

    def __init__(self, name, is_human, ocean, opponent_ocean):
        self.name = name
        self.ocean = ocean
        self.opponent_ocean = opponent_ocean
        self.is_human = is_human
        self.name = name
        self.start_time = time()

    def put_ship_on_board(self, ship_name, is_horizontal, starting_point):
        eval(ship_name)(self.is_human, self.ocean, is_horizontal, starting_point)

    def player_turn(self):
        print('Turn: ', self.name)
        print(self.ocean)
        print('Opponent ocean:')
        print(self.opponent_ocean)

    def shot_outcome(self, positions):
        row = positions[0]
        line = positions[1]
        print(row, line)
        if not isinstance(self.opponent_ocean.board[line][row], ShipSquare):
            self.opponent_ocean.board[line][row].change_sign('0')
            print('Shot missed')
            return False
        else:
            self.opponent_ocean.board[line][row].change_sign('X')
            print('Hit!')
            return True

    def ai_guess(self, difficulty_level, player_ocean, player):
        print("Computer turn")
        player_ships_sign = ["BA", "CA", "CR", "SU", "DE"]

        while True:

            hit_success = random.randint(0, 50 * int(difficulty_level))

            if hit_success > 50:

                for line in player_ocean.board:

                    for square in line:
                        if isinstance(square, ShipSquare):
                            square.change_sign('X')
                            print('Hit!')
                            print(player_ocean)
                            break

            else:
                row = random.randint(1, 8)
                line = random.randint(1, 8)
                positions = [row, line]
                print('Shot at: ' + str(row) + str(line) + 'outcome: ')
                if not self.shot_outcome(positions):
                    break

            for sign in player_ships_sign:
                    if player.check_if_ship_is_destroyed(sign, player_ocean):
                        print("Your ship: " + sign + "has been sunk!")
                        player_ships_sign.remove(sign)

            if not player_ships_sign:
                    "You lose!"
                    return True

    def __str__(self):
        return self.name

