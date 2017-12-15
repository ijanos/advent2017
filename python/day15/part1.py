#!/usr/bin/env python3

from itertools import islice

def generator(seed, A):
    n = seed
    factor = 16807 if A else 48271
    while True:
        n = n * factor
        n = n % 2147483647
        yield n

A = generator(634, True)
B = generator(301, False)

mask = 0b1111111111111111
part1 = sum(a & mask == b & mask for a, b in islice(zip(A, B), 40_000_000))
print(part1)
