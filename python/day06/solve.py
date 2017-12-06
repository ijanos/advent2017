#!/usr/bin/env python3

import fileinput

mem = [int(n.strip()) for n in next(fileinput.input()).split()]
size = len(mem)

states = set()
states.add('.'.join(str(n) for n in mem))
part2 = None
steps = 0

while True:
    i = mem.index(max(mem))
    x = mem[i]
    mem[i] = 0
    while x > 0:
        i += 1
        mem[i % size] += 1
        x -= 1
    steps += 1
    statehash = '.'.join(str(n) for n in mem)
    if statehash in states:
        if not part2:
            print("Part 1:", steps)
            part2 = statehash
            part1_steps = steps
        else:
            if statehash == part2:
                print("Part 2:", steps - part1_steps)
                break
    else:
        states.add(statehash)
