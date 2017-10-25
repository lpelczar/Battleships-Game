from texttable import *
from game import *
from ship import *
import os


def import_highscore():
    new_line_position = -1
    highscore = []

    with open('highscore.csv', 'r') as file:
        for line in file:
            highscore.append(line[:new_line_position].split(','))
    return highscore


def export_highscore(highscore):

    with open('highscore.csv', 'w') as file:
        writer = csv.writer(file)
        for line in highscore:
            writer.writerow(line)


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
            table = Texttable()
            table.set_deco(Texttable.HEADER)
            table.set_cols_align(["l", "l"])
            table.add_rows(highscore)
            print(table.draw())

        elif option == '4':
            exit("Thanks for playing.")


if __name__ == "__main__":
    #main()



    ocean = Ocean()
    player = Player('bot', False, ocean)
    player.add_ship_to_ocean()
    #player.add_ship_to_ocean()
    print(ocean)
