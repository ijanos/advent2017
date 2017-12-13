#!/usr/bin/env python3

import fileinput
from collections import deque

firewall = {}
last = 0
for line in fileinput.input():
    depth, runrange = (int(n.strip(':')) for n in line.split())
    firewall[depth] = deque(list(range(0, runrange)) + list(range(runrange - 2, 0, -1)))
    last = max(depth, last)


severity = 0

for i in range(last+1):
    if i in firewall and firewall[i][0] == 0:
        severity += i * ((len(firewall[i]) + 2) // 2)
    for k in firewall:
        firewall[k].rotate()

print("Part 1:", severity)

