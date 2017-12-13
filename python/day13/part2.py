#!/usr/bin/env python3

import fileinput
from collections import deque
from copy import deepcopy


firewall = {}
last = 0
for line in fileinput.input():
    depth, runrange = (int(n.strip(':')) for n in line.split())
    firewall[depth] = deque(list(range(0, runrange)) + list(range(runrange - 2, 0, -1)))
    last = max(depth, last)


success = False
wait = 0

while not success:
    success = True
    wait += 1
    fw = deepcopy(firewall)
    for k in fw:
        fw[k].rotate(wait)
    for i in range(last + 1):
        if i in fw and fw[i][0] == 0:
            success = False
            break
        for k in fw:
            fw[k].rotate()

print(wait)
