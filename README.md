# Battleship in the OOP way

## Story

The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates. Neither you nor the other player can see the other's board so you must try to guess where they are.

Each player places the 5 ships somewhere on their board. The board is a square with side's length equals 10 (spaces). The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship. Ships may not touch each other.

The 5 ships are: Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).

You sets ships by enter ship's name, answer the question if it's horizontal and the number of space which it occupies. You can add only one ship of each kind.

Once the guessing begins, the players may not move the ships.

## Features

- Two game modes: Single player (PvC), Multiplayer (Hot Seat).
- 3 difficulty levels (easy, medium, hard).
- Computer "AI"
- Hall of fame

## Sample screenshots

![c1](http://i63.tinypic.com/2rppqtt.png)
![c2](http://i64.tinypic.com/25f20x2.png)

## Installation

Use Python 3.6 version and start main.py in console

```
python3.6 main.py
```

## More info

Project made for [Codecool](https://codecool.com/) programming course.
