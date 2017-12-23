import re
import sys
import numpy as np

with open("particle.txt") as f:
    content = f.readlines()


class Particle:
    def __init__(self, arr):
        self.p = np.array(arr[0:3])
        self.v = np.array(arr[3:6])
        self.a = np.array(arr[6:9])

    def position(self, time):
        t_pos = self.p + self.v * time + self.a * time * time // 2
        return abs(t_pos).sum()


reg = re.compile(r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, '
                 r'a=<(-?\d+),(-?\d+),(-?\d+)>')

particles = [Particle([int(y) for y in reg.match(x.strip()).groups()]) for x in content]

min_ind = -1
min_val = sys.maxsize
for p, ind in zip(particles, range(len(particles))):
    pos = p.position(1000)
    if pos < min_val:
        min_val = pos
        min_ind = ind


print(min_ind)

