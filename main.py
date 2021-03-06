import os

from game import *
from highscore import HighScoreManager


def main():
    """
    Handle menu options
    """
    os.system('clear')

    while True:
        os.system('clear')
        option = input('''
                             ______________________________________________
                          .-'                     _                        '.
                        .'                       |-'                        |
                      .'                         |                          |
                   _.'               p         _\_/_         p              |
                _.'                  |       .'  |  '.       |              |
           __..'                     |      /    |    \      |              |
     ___..'                         .T\    ======+======    /T.             |
  ;;;\::::                        .' | \  /      |      \  / | '.           |
  ;;;|::::                      .'   |  \/       |       \/  |   '.         |
  ;;;/::::                    .'     |   \       |        \  |     '.       |
        ''.__               .'       |    \      |         \ |       '.     |
             ''._          <_________|_____>_____|__________>|_________>    |
                 '._     (___________|___________|___________|___________)  |
                    '.    \;;;;;;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;/   |
                      '.~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   |
                        '. ~ ~ ~ ~ ~ ~ ~ ~ ~Battleship ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
                          '-.______________________________________________.'


Choose option:
(1) Start single player
(2) Start multi player
(3) Show highscores
(4) exit
''')
        if option == '1':
            os.system('clear')

            player_name = input('Enter player name: ')
            difficulty_level = None
            while True:
                try:
                    os.system('clear')
                    difficulty_level = int(input('Enter difficulty of computer player(0:easy, 1:medium, 2:hard): '))
                    if difficulty_level in [0, 1, 2]: break
                except:
                    continue
            os.system('clear')
            singleplayer_game = SingleGame(player_name, difficulty_level)
            singleplayer_game.start_game()

        elif option == '2':
            os.system('clear')

            player_name1 = input('Enter name of 1st player: ')
            player_name2 = input('Enter name of 2nd player: ')

            multiplayer_game = MultiPlayerGame(player_name1, player_name2)
            multiplayer_game.start_game()

        elif option == '3':
            os.system('clear')
            HighScoreManager.print_highscore()
            input('Press enter to return')

        elif option == '4':
            os.system('clear')
            exit("Thanks for playing.")


if __name__ == "__main__":
    main()
