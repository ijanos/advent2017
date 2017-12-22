#!/usr/bin/env python3

import fileinput
from operator import add
from collections import defaultdict

UP, RIGHT, DOWN, LEFT = range(4)

turnleft = lambda d: (d - 1) % 4
turnright = lambda d: (d + 1) % 4

grid = defaultdict(lambda: '.')

move = {
    UP: (0, -1),
    RIGHT: (1, 0),
    DOWN: (0, 1),
    LEFT: (-1, 0)
}

GRIDOFFSET = 12

for y, line in enumerate(fileinput.input()):
    for x, node in enumerate(line.strip()):
        grid[(x - GRIDOFFSET, y - GRIDOFFSET)] = node

heading = UP
part1 = 0
pos = (0, 0)

for _ in range(10_000):
    if grid[pos] == '#':
        heading = turnright(heading)
        grid[pos] = '.'
    else:
        heading = turnleft(heading)
        grid[pos] = '#'
        part1 += 1
    pos = tuple(map(add, pos, move[heading]))


print("Part 1:", part1)
