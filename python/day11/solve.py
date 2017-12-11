#!/usr/bin/env python3

import fileinput
from operator import add

move = {
    "n":  ( 1,  0, -1),
    "ne": ( 1, -1,  0),
    "se": ( 0, -1,  1),
    "s":  (-1,  0,  1),
    "sw": (-1,  1,  0),
    "nw": ( 0,  1, -1)
}

cur = (0, 0, 0)
furthest = 0

for line in fileinput.input():
    for d in line.strip().split(','):
        cur = tuple(map(add, cur, move[d]))
        distance = sum(map(abs, cur)) // 2
        furthest = max(distance, furthest)

print("Part 1:", distance)
print("Part 2:", furthest)
