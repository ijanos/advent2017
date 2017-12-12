#!/usr/bin/env python3

import fileinput

connections = {}

for line in fileinput.input():
    left, _, right = line.strip().split(maxsplit=2)
    right = [r.strip() for r in right.split(',')]
    connections[left] = right

current = ['0']
visited = set(current)

while current:
    e = current.pop()
    notyetseen = [p for p in connections[e] if p not in visited]
    current += notyetseen
    visited.update(notyetseen)

print("Part 1: ", len(visited))

visited = set()
part2 = 0

for p in connections:
    if p in visited:
        continue
    else:
        part2 += 1
        visited.update([p])
        cur = [p]
        while cur:
            e = cur.pop()
            new = [p for p in connections[e] if p not in visited]
            cur += new
            visited.update(new)

print("Part 2:", part2)
