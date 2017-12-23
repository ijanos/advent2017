#!/usr/bin/env python3

import fileinput
from collections import defaultdict


program = []

for line in fileinput.input():
    cmd = line.strip().split()
    ins = cmd[0]
    val0 = cmd[1] if cmd[1].isalpha() else int(cmd[1])
    val1 = cmd[2] if cmd[2].isalpha() else int(cmd[2])
    program.append((ins, val0, val1))


pc = 0
reg = defaultdict(int)
part1 = 0

def value(x):
    if isinstance(x, int):
        return x
    else:
        return reg[x]

while pc < len(program):
    ins, val0, val1 = program[pc]
    if ins == 'set':
        reg[val0] = value(val1)
    elif ins == 'sub':
        reg[val0] -= value(val1)
    elif ins == 'mul':
        reg[val0] *= value(val1)
        part1 += 1
    elif ins == 'jnz':
        if value(val0) != 0:
            pc += (value(val1) - 1)
    pc += 1

print("Part 1:", part1)
