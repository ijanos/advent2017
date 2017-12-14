#!/usr/bin/env python3

from collections import deque
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

used = 0
for i in range(128):
    key = f"{PUZZLE}-{i}"
    used += ''.join('{:08b}'.format(n) for n in knot(key)).count('1')

print("Part 1:", used)
