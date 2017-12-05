#!/usr/bin/env python3

import fileinput

p1 = 0
p2 = 0

for line in fileinput.input():
    line = line.strip().split()
    if len(set(line)) == len(line):
        p1 += 1

    line = [''.join(sorted(word)) for word in line]
    if len(set(line)) == len(line):
        p2 += 1

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
