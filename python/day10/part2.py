#!/usr/bin/env python3

from collections import deque
from itertools import islice

INPUT = "18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"
INPUT = [ord(n) for n in INPUT]
INPUT += [17, 31, 73, 47, 23]

LIST = deque(range(256))
SKIP = 0
rotate_sum = 0

for _ in range(64):
    for length in INPUT:
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

print("Part 2:", ''.join('{:02X}'.format(n) for n in dense).lower())
