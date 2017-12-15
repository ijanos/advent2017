#!/usr/bin/env python3

from itertools import islice

def generator(seed, A):
    n = seed
    factor = 16807 if A else 48271
    criteria = 4 if A else 8
    while True:
        n = n * factor
        n = n % 2147483647
        if n % criteria == 0:
            yield n

A = generator(634, True)
B = generator(301, False)

mask = 0b1111111111111111
part2 = sum(a & mask == b & mask for a, b in islice(zip(A, B), 5_000_000))
print(part2)
