# Battleship in the OOP way

## The story

The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates. Neither you nor the other player can see the other's board so you must try to guess where they are.

Each player places the 5 ships somewhere on their board. The board is a square with side's length equals 10 (spaces). The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship. Ships may not touch each other.

The 5 ships are: Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).

You sets ships by enter ship's name, answer the question if it's horizontal and the number of space which it occupies. You can add only one ship of each kind.

Once the guessing begins, the players may not move the ships.

## Specification

Read the md file in specifications folder with appropriate name.

__main.py__

__square.py__

__ship.py__

__ocean.py__

__player.py__

__keygetch.py__

__textable.py__

__highscore.py__

__game.py__
