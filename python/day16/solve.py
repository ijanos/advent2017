#!/usr/bin/env python3

import fileinput
from collections import deque
from string import ascii_lowercase


def dance(moves, times=1):
    order = deque(ascii_lowercase[0:16])
    cache = {}
    for _ in range(times):
        start_state = ''.join(order)
        if start_state in cache:
            order = deque(cache[start_state])
            continue
        for cmd, move in moves:
            if cmd == 's':
                order.rotate(move)
            elif cmd == 'x':
                i, j = move
                order[i], order[j] = order[j], order[i]
            else:
                x, y = move
                i = order.index(x)
                j = order.index(y)
                order[i], order[j] = y, x
        cache[start_state] = ''.join(order)
    return ''.join(order)


moves = []
for line in fileinput.input():
    for move in line.strip().split(','):
        cmd = move[0]
        if cmd == 's':
            moves.append(('s', int(move[1:])))
        elif cmd == "x":
            i, j = (int(n) for n in move[1:].split('/'))
            moves.append(('x', (i, j)))
        else:
            i, j = move[1:].split('/')
            moves.append(('p', (i, j)))


print("Part 1:", dance(moves))
print("Part 2:", dance(moves, 1_000_000))
