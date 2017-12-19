#!/usr/bin/env python3

import fileinput
from operator import add


route = {}
pos = None

for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line.strip('\n')):
        if c is not ' ':
            if not pos:
                pos = (x, y)
            route[(x, y)] = c

UP, DOWN, LEFT, RIGHT = range(4)

heading = DOWN

move = {
    UP:    ( 0, -1),
    DOWN:  ( 0,  1),
    LEFT:  ( 1,  0),
    RIGHT: (-1,  0)
}

opposite = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}

part1 = []

run = True
steps = 0

while run:
    steps += 1
    if route[pos].isalpha():
        part1.append(route[pos])

    nextpos = tuple(map(add, pos, move[heading]))

    if nextpos in route:
        pos = nextpos
    else:
        for newheading in move:
            run = True
            lookahead = tuple(map(add, pos, move[newheading]))
            if newheading != opposite[heading] and lookahead in route:
                pos = lookahead
                heading = newheading
                break
            run = False

print("Part 1:", ''.join(part1))
print("Part 2:", steps)
