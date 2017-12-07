#!/usr/bin/env python3

import fileinput
from itertools import chain
from collections import defaultdict, namedtuple

programs = {}
Program = namedtuple('Program', ['weight', "children"])

for line in fileinput.input():
    line = line.strip().split(maxsplit=3)
    name, weight = line[0], int(line[1].strip('()'))
    if len(line) > 2:
        children = [child.strip() for child in line[3].split(',')]
    else:
        children = []
    programs[name] = Program(weight, children)

names = programs.keys()
all_children = chain(*[p.children for p in programs.values()])

part1 = (set(names) - set(all_children)).pop()
print("Part 1:", part1)

def calc_weight(name):
    return programs[name].weight + sum(calc_weight(child) for child in programs[name].children)

cur = part1
diff = 0

while True:
    bins = defaultdict(list)
    for child in programs[cur].children:
        bins[calc_weight(child)].append(child)
    if len(bins) > 1:
        (w0, wrong), (w1, _) = sorted(bins.items(), key=lambda i: len(i[1]))
        cur = wrong.pop()
        diff = w1 - w0
    else:
        break

print("Part 2:", programs[cur].weight + diff)
