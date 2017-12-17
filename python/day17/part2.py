#!/usr/bin/env python3

from collections import deque

INPUT = 324

spinlock = deque()

for n in range(50_000_000):
    spinlock.append(n)
    spinlock.rotate(-INPUT)

print(spinlock[spinlock.index(0) + 1])