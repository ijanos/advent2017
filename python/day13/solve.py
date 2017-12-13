#!/usr/bin/env python3

import fileinput


firewall = []

for line in fileinput.input():
    depth, runrange = (int(n.strip(':')) for n in line.split())
    runrange = 2 * runrange - 2
    firewall.append((depth, runrange))

def run(delay, fast=False):
    severity = 0
    caught = False
    for i, runrange in firewall:
        if (i + delay) % runrange == 0:
            caught = True
            if fast:
                break
            severity += i * ((runrange + 2) // 2)
    return (caught, severity)

caught, part1 = run(0)
print("Part 1:", part1)

wait = 0
while caught:
    caught, _ = run(wait, fast=True)
    wait += 1

print("Part 2:", wait)