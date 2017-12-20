#!/usr/bin/env python3

import fileinput
from operator import add
from collections import Counter

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
    collision_positions = [pos for pos, n in Counter(p.p for p in particles).items() if n > 1]
    particles = [p for p in particles if p.p not in collision_positions]

print("Part 2:", len(particles))
