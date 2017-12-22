#!/usr/bin/env python3

import fileinput
from operator import add
from collections import defaultdict

UP, RIGHT, DOWN, LEFT = range(4)

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
pos = (0, 0)

step = {
    '#': ('F', lambda d: (d + 1) % 4),
    '.': ('W', lambda d: (d - 1) % 4),
    'W': ('#', lambda n: n),
    'F': ('.', lambda d: (d + 2) % 4)
}

part2 = 0
for _ in range(10_000_000):
    new, turn = step[grid[pos]]
    heading = turn(heading)
    grid[pos] = new
    part2 += 1 if new == '#' else 0
    pos = tuple(map(add, pos, move[heading]))

print("Part 2:", part2)
