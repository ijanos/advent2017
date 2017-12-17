#!/usr/bin/env python3

from collections import deque

INPUT = 324

spinlock = deque()

for n in range(2017):
    spinlock.append(n)
    spinlock.rotate(-INPUT)

print(spinlock[0])
