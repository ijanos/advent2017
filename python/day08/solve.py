#!/usr/bin/env python3

import fileinput
from collections import defaultdict

cpu = defaultdict(lambda: 0)

compare = {
    "<": lambda ab: ab[0] < ab[1],
    ">": lambda ab: ab[0] > ab[1],
    ">=": lambda ab: ab[0] >= ab[1],
    "<=": lambda ab: ab[0] <= ab[1],
    "==": lambda ab: ab[0] == ab[1],
    "!=": lambda ab: ab[0] != ab[1]
}

highest = 0

for line in fileinput.input():
    line = line.strip().split()
    reg, op, val, _, cond_reg, cond_op, cond_val = line
    val = int(val)
    cond_val = int(cond_val)
    if compare[cond_op]((cpu[cond_reg], cond_val)):
        if op == "dec":
            val = -val
        cpu[reg] += val
    if cpu[reg] > highest:
        highest = cpu[reg]


part1 = max(cpu.values())
print("Part 1:", part1)
print("Part 2:", highest)
