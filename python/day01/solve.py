#!/bin/env python3

import fileinput
from collections import deque

def get_sum(list1, list2):
    ret = 0
    for p1, p2 in zip(list1, list2):
        if p1 == p2:
            ret += int(p1)
    return ret

if __name__ == "__main__":
    puzzle = next(fileinput.input()).strip()

    puzzle_rot1 = deque(puzzle)
    puzzle_rot1.rotate(-1)
    part1 = get_sum(puzzle, puzzle_rot1)

    puzzle_halfrot = deque(puzzle)
    puzzle_halfrot.rotate(len(puzzle)//2)
    part2 = get_sum(puzzle, puzzle_halfrot)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
