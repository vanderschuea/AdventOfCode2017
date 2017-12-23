import re
import numpy as np

with open("particle.txt") as f:
    content = f.readlines()


class Particle:
    def __init__(self, arr):
        self.p = np.array(arr[0:3])
        self.v = np.array(arr[3:6])
        self.a = np.array(arr[6:9])
        self.active = True

    def update(self):
        self.v += self.a
        self.p += self.v

    def delete(self):
        self.active = False


reg = re.compile(r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, '
                 r'a=<(-?\d+),(-?\d+),(-?\d+)>')


particles = [Particle([int(y) for y in reg.match(x.strip()).groups()]) for x in content]

for _ in range(50):
    dic = {}
    for p, ind in zip(particles, range(len(particles))):
        if p.active:
            p.update()
            h = str(p.p)
            if h not in dic:
                dic[h] = p
            else:
                p.delete()
                dic[h].delete()

tot = 0
for p in particles:
    tot += p.active
print(tot)

