#!/usr/bin/env python3

import fileinput
from collections import defaultdict


program = []

for line in fileinput.input():
    cmd = line.strip().split()
    ins = cmd[0]
    val0 = cmd[1] if cmd[1].isalpha() else int(cmd[1])
    if len(cmd) == 3:
        val1 = cmd[2] if cmd[2].isalpha() else int(cmd[2])
        program.append((ins, val0, val1))
    else:
        program.append((ins, val0))



pc = 0
reg = defaultdict(int)
sound = 0

def value(x):
    if isinstance(x, int):
        return x
    else:
        return reg[x]

while pc < len(program):
    cmd = program[pc]
    if cmd[0] == 'snd':
        sound = value(cmd[1])
    elif cmd[0] == 'set':
        reg[cmd[1]] = value(cmd[2])
    elif cmd[0] == 'add':
        reg[cmd[1]] += value(cmd[2])
    elif cmd[0] == 'mul':
        reg[cmd[1]] *= value(cmd[2])
    elif cmd[0] == 'mod':
        reg[cmd[1]] %= value(cmd[2])
    elif cmd[0] == 'rcv':
        if value(cmd[1]):
            break
    elif cmd[0] == 'jgz':
        if value(cmd[1]) > 0:
            pc += (value(cmd[2]) - 1)
    pc += 1

print("Part 1:", sound)
