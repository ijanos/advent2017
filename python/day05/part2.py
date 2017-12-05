#!/usr/bin/env python3

import fileinput

jumps = [int(line.strip()) for line in fileinput.input()]

pc = 0
steps = 0

while pc < len(jumps):
    i = jumps[pc]
    if i > 2:
        jumps[pc] -= 1
    else:
        jumps[pc] += 1
    pc += i
    steps += 1

print(f"Part 2: {steps}")
