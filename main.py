from texttable import *
from game import *


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
    highscore = import_highscore()

    while True:
        option = input('''
        Choose option:
        (1) Start single player
        (2) Start multi player
        (3) Show highscores
        (4) exit''')

        if option == '1':
            ...
        elif option == '2':
            ...
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
    player = Player(' ', False, ocean)
    player.add_ship_to_ocean()
    print(ocean)