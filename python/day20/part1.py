#!/usr/bin/env python3

import fileinput
from operator import add

particles = []

class Particle():
    def __init__(self, i, p, v, a):
        self.id = i
        self.p = p
        self.v = v
        self.a = a

    def __repr__(self):
        return f"Point#{self.id} p={self.p} v={self.v} a={self.a}"

    def move(self):
        self.v = tuple(map(add, self.v, self.a))
        self.p = tuple(map(add, self.p, self.v))

    def distance(self):
        return sum(abs(n) for n in self.p)

for i, line in enumerate(fileinput.input()):
    line = line.strip().split(',')
    x, y, z, vx, vy, vz, ax, ay, az = (int(n.strip(' avp=<>')) for n in line)
    particles.append(Particle(i, (x, y, z), (vx, vy, vz), (ax, ay, az)))

for _ in range(500):
    for p in particles:
        p.move()

print("Part 1:", min(particles, key=lambda p: p.distance()).id)
