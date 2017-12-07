#!/usr/bin/env python3

import fileinput
from itertools import chain
from collections import defaultdict

programs = {}
for line in fileinput.input():
    line = line.strip().split(maxsplit=3)
    name, weight = line[0], int(line[1].strip('()'))
    if len(line) > 2:
        children = [child.strip() for child in line[3].split(',')]
    else:
        children = []
    programs[name] = (weight, children)

names = programs.keys()
all_children = chain(*[children for _, children in programs.values()])

part1 = (set(names) - set(all_children)).pop()
print("Part 1:", part1)

def calc_weight(n):
    return programs[n][0] + sum(calc_weight(child) for child in programs[n][1])

cur = part1
diff = 0
while True:
    bins = defaultdict(list)
    for child in programs[cur][1]:
        bins[calc_weight(child)].append(child)
    if len(bins) > 1:
        cur = min(bins.values(), key=len).pop()
        v1, v2 = bins.keys()
        diff = abs(v1 - v2)
    else:
        break

print("Part 2:", programs[cur][0] - diff)
