from texttable import *
from game import *
import os


def import_highscore():

    highscore = []

    with open('highscore.csv', 'r') as file:
        for line in file:
            highscore.append(line.split(','))
    for line in highscore:
        print(line)
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
        option = input('''
        Choose option:
        (1) Start singleplayer
        (2) Start multiplayer
        (3) Show highscores
        (4) Exit\n''')

        if option == '1':
            ...

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
    main()
