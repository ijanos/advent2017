#!/usr/bin/env python3

import fileinput
from collections import deque
from copy import deepcopy


firewall = {}
last = 0

for line in fileinput.input():
    depth, runrange = (int(n.strip(':')) for n in line.split())
    firewall[depth] = 2 * runrange - 2
    last = max(depth, last)

def run(delay, fast=False):
    severity = 0
    caught = False
    for i in range(last+1):
        if i in firewall and (i + delay) % firewall[i] == 0:
            severity += i * ((firewall[i] + 2) // 2)
            caught = True
            if fast:
                break
    return (caught, severity)

(_, part1) = run(0)
print("Part 1:", part1)

wait = 0
while True:
    (caught, _) = run(wait, fast=True)
    if not caught:
        break
    wait += 1

print("Part 2:", wait)