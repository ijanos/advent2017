#!/usr/bin/env python3

from operator import add, abs
from math import floor
from collections import defaultdict

INPUT = 361527

# 0 - RIGHT
# 1 - UP
# 2 - LEFT
# 3 - DOWN

class Cursor:
    def __init__(self):
        self.direction = 0
        self.coord = (0, 0)

    def turn(self):
        self.direction = (self.direction + 1) % 4

    def move(self):
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
    square_map = defaultdict(lambda: 0)
    square_map[(0,0)] = 1

    while True:
        cur.move()
        square_map[cur.coord]
        neigboursum = 0
        for n in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            neigboursum += square_map[tuple(map(add, cur.coord, n))]
        square_map[cur.coord] = neigboursum
        if neigboursum > INPUT:
            print(f"Part 2: {neigboursum}")
            break
        if run_length == floor(side_length):
            cur.turn()
            run_length = 0
            side_length += 0.5
        run_length += 1
