from square import *

class Ocean():

    def __init__(self):
        self.ocean = []
        self.create_board()

    def create_board(self, height=10, width=10):
        for c in range(0, height):
            self.ocean.append([OceanSquare() for i in range(width)])

        for k,v in enumerate(self.ocean):
            if k == 0 or k == height-1:
                for c,x in enumerate(v):
                    v[c] = BorderSquare()
            else:
                for c,x in enumerate(v):
                    if c == 0 or c == width-1:
                        v[c] = BorderSquare()

    def __str__(self):
        return "\n".join([str(i) for i in self.ocean])