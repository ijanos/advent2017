#!/usr/bin/env python3

import fileinput
from enum import Enum
from collections import deque

class State(Enum):
    COUNT = 1
    GARBAGE = 2
    IGNORE = 3


STATE = State.COUNT
DEPTH = 0
PART1_SUM = 0
PART2_SUM = 0

for line in fileinput.input():
    line = deque(line.strip())
    while line:
        c = line.popleft()
        if STATE == State.COUNT:
            if c == '{':
                DEPTH += 1
            elif c == '}':
                PART1_SUM += DEPTH
                DEPTH -= 1
            elif c == '<':
                STATE = State.GARBAGE
        elif STATE == State.GARBAGE:
            if c == '>':
                STATE = State.COUNT
            elif c == '!':
                STATE = State.IGNORE
            else:
                PART2_SUM += 1
        else:
            STATE = State.GARBAGE

print("Part 1:", PART1_SUM)
print("Part 2:", PART2_SUM)
