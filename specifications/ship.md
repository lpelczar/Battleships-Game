### Class Ship

__Instance Attributes__

* `space`
- data: int
- description: Length of a ship

* `sign`
- data: str
- description: String representation of a ship

* `player_create`
- data: bool
- description: True if player is creating ship, False if computer is creating ship

* `ocean`
- data: Ocean
- description: Ocean where the ship is placed

* `is_horizontal`
- data: bool
- description: True if ship is placed horizontal, False if it is placed vertical

* `starting_point`
- data: tuple
- description: Tuple with starting point of a ship (row, line)

* `is_decoy`
- data: bool
- description: True if you are placing ship on additional temp board default: False

__Instance methods__

* ##### `__init__(self, space: int, sign: str, player_create: bool, ocean: Ocean, is_horizontal: bool, starting_point: (int, int), is_decoy=False)`

Class representing Ship object on board

* `create_ship_by_user(self, starting_point)`

Check if ship can be placed here and add ship on board:

The ships can only be placed vertically or horizontally.
Diagonal placement is not allowed.
No part of a ship may hang off the edge of the board.
Ships may not overlap each other.
No ships may be placed on another ship. Ships may not touch each other.

* `create_ship_by_decoy(self, position)`

Used for moving ship while placing it, to do it we create temporary additional ocean

* `is_another_ship_near(self, x, y)`

Check if there is another ship around ship with given position

* `create_ship_by_computer(self)`

Place randomly all ships on the board.

* `__str__(self)`

### Class Carrier(Ship)

* `__init__`

### Class Battleship(Ship)

* `__init__`

### Class Cruiser(Ship)

* `__init__`

### Class Submarine(Ship)

* `__init__`

### Class Destroyer(Ship)

* `__init__`
