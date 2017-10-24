from texttable import *
from game import *


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
    highscore = import_highscore()

    while True:
        option = input('''
Choose option:
(1) Start single player
(2) Start multi player
(3) Show highscores
(4) exit''')

        if option == '1':
            name = input('Type in your name: ')
            difficulity_level = int(input('''
            
Select difficulity:
(1) Easy
(2) Medium
(3) Hard'''))

        elif option == '2':
            first_player_name = input('Type in first player name: ')
            second_player_name = input('Type in second player name: ')

            MultiPlayerGame(first_player_name, second_player_name)

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
