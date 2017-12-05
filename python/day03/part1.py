#!/usr/bin/env python3

from operator import add, abs
from math import floor

INPUT = 361527

# 0 - RIGHT
# 1 - UP
# 2 - LEFT
# 3 - DOWN

class Cursor:
    def __init__(self):
        self.n = 1
        self.direction = 0
        self.coord = (0, 0)

    def turn(self):
        self.direction = (self.direction + 1) % 4

    def move(self):
        self.n += 1
        offset = {
            0: ( 1,  0),
            1: ( 0,  1),
            2: (-1,  0),
            3: ( 0, -1)
        }
        self.coord = tuple(map(add, self.coord, offset[self.direction]))

if __name__ == "__main__":
    cur = Cursor()
    side_length = 1
    run_length = 1
    while cur.n != INPUT:
        cur.move()
        if run_length == floor(side_length):
            cur.turn()
            run_length = 0
            side_length += 0.5
        run_length += 1
    (x, y) = cur.coord
    p1 = abs(x) + abs(y)
    print(f"Part 1: {p1}")
