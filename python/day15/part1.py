#!/usr/bin/env python3

from itertools import islice

def generator(n, factor):
    while True:
        n = n * factor % 2147483647
        yield n & 0xFFFF

A = generator(634, 16807)
B = generator(301, 48271)

part1 = sum(a == b for a, b in islice(zip(A, B), 40_000_000))
print(part1)
