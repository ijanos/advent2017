#!/usr/bin/env python3

# python3 converter.py | python3 ../day12/solve.py

from collections import deque, defaultdict
from itertools import islice

def knot(key):
    key = [ord(n) for n in key]
    key += [17, 31, 73, 47, 23]

    LIST = deque(range(256))
    SKIP = 0
    rotate_sum = 0

    for _ in range(64):
        for length in key:
            head = []
            for _ in range(length):
                head.append(LIST.popleft())
            LIST.extendleft(head)
            LIST.rotate(-(length + SKIP))
            rotate_sum += length + SKIP
            SKIP += 1

    LIST.rotate(rotate_sum)
    dense = []
    for i in range(16):
        element = 0
        for n in islice(LIST, i*16, i*16+16):
            element ^= n
        dense.append(element)
    return dense

PUZZLE = 'nbysizxe'

grid = set()
for y in range(128):
    key = f"{PUZZLE}-{y}"
    for x, n in enumerate(''.join('{:08b}'.format(n) for n in knot(key))):
        if n == '1':
            grid.add((x, y))

for x, y in grid:
    connections = []
    for offx, offy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if (x+offx, y+offy) in grid:
            connections.append(str(128*(y+offy) + (x+offx)))
    left = 128*y + x
    right = ','.join(connections) if connections else left
    print(f"{left} <-> {right}")
