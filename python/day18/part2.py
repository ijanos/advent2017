#!/usr/bin/env python3

import fileinput
from collections import defaultdict, deque


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

class CPU():
    def __init__(self, id, sendq, recvq):
        self.pc = 0
        self.reg = defaultdict(int)
        self.reg['p'] = id
        self.send = sendq
        self.recv = recvq
        self.sendcount = 0
        self.wait = False

    def val(self, x):
        if isinstance(x, int):
            return x
        else:
            return self.reg[x]

    def step(self):
        if self.pc < len(program):
            cmd = program[self.pc]
            if cmd[0] == 'snd':
                self.send.appendleft(self.val(cmd[1]))
                self.sendcount += 1
            elif cmd[0] == 'set':
                self.reg[cmd[1]] = self.val(cmd[2])
            elif cmd[0] == 'add':
                self.reg[cmd[1]] += self.val(cmd[2])
            elif cmd[0] == 'mul':
                self.reg[cmd[1]] *= self.val(cmd[2])
            elif cmd[0] == 'mod':
                self.reg[cmd[1]] %= self.val(cmd[2])
            elif cmd[0] == 'rcv':
                if self.recv:
                    self.reg[cmd[1]] = self.recv.pop()
                    self.wait = False
                else:
                    self.wait = True
                    self.pc -= 1
            elif cmd[0] == 'jgz':
                if self.val(cmd[1]) > 0:
                    self.pc += self.val(cmd[2]) - 1
            self.pc += 1


q0, q1 = deque(), deque()

cpu0 = CPU(0, q0, q1)
cpu1 = CPU(1, q1, q0)

while True:
    cpu0.step()
    cpu1.step()
    if cpu0.wait and cpu1.wait:
        break

print("Part 2:", cpu1.sendcount)
