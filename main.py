from texttable import *
from game import *
import os
from highscore import HighScoreManager


def main():
    # highscore = import_highscore()
    os.system('clear')

    while True:
        option = input('''Choose option:
(1) Start single player
(2) Start multi player
(3) Show highscores
(4) exit
''')

        if option == '1':
            os.system('clear')

            player_name = input('Enter player name: ')
            difficulty_level = input('Enter difficulty of computer player(0:easy, 1:medium, 2:hard):\n')

            singleplayer_game = SingleGame(player_name, difficulty_level)
            singleplayer_game.start_game()

        elif option == '2':
            os.system('clear')

            player_name1 = 'Zosia'  # input('Enter name of 1st player: ')
            player_name2 = 'Jasio'  # input('Enter name of 2nd player: ')

            multiplayer_game = MultiPlayerGame(player_name1, player_name2)
            multiplayer_game.start_game()

        elif option == '3':
            HighScoreManager.print_highscore()

        elif option == '4':
            exit("Thanks for playing.")


if __name__ == "__main__":
    main()

    # ocean = Ocean()
    # ocean.put_all_ships_for_bot()
    # player = Player('bot', False, ocean, None)
    # print(ocean)
