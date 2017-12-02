#!/bin/env python3

import fileinput
from itertools import combinations

if __name__ == "__main__":
    p1_sum = 0
    p2_sum = 0
    for line in fileinput.input():
        line = line.strip()
        line = [int(n) for n in line.split()]
        p1_sum += max(line) - min(line)
        for n1, n2 in combinations(line, 2):
            if n1 % n2 == 0 or n2 % n1 == 0:
                p2_sum += max(n1, n2) // min(n1, n2)
                break
    print(f"Part 1: {p1_sum}")
    print(f"Part 2: {p2_sum}")
