#!/usr/bin/env python3

from collections import deque

INPUT = [18, 1, 0, 161, 255, 137, 254, 252, 14, 95, 165, 33, 181, 168, 2, 188]

LIST = deque(range(256))
SKIP = 0
rotate_sum = 0

for length in INPUT:
    head = []
    for _ in range(length):
        head.append(LIST.popleft())
    LIST.extendleft(head)
    LIST.rotate(-(length + SKIP))
    rotate_sum += length + SKIP
    SKIP += 1

LIST.rotate(rotate_sum)
print("Part 1:", LIST[0] * LIST[1])
