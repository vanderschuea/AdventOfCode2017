from enum import Enum
from collections import defaultdict


class Face:
    def __init__(self, x, y):
        self.dir = [0, -1]
        self.x = x
        self.y = y

    def left(self):
        d = self.dir
        if d == [0, -1]: self.dir = [-1, 0]
        elif d == [0, 1]: self.dir = [1, 0]
        elif d == [-1, 0]: self.dir = [0, 1]
        elif d == [1, 0]: self.dir = [0, -1]

    def right(self):
        self.left()
        self.dir = [-self.dir[0], -self.dir[1]]

    def move(self):
        self.x += self.dir[1]
        self.y += self.dir[0]


with open('virus.txt') as f:
    content = f.readlines()
temp_map = [list(line.strip()) for line in content]
virus_map = defaultdict(bool)
for y in range(len(temp_map)):
    for x in range(len(temp_map[0])):
        if temp_map[y][x] == '#':
            virus_map[str([x, y])] = True
face = Face(len(temp_map)//2, len(temp_map[0])//2)

caused_infections = 0
for _ in range(10000):
    x, y = face.x, face.y
    xy_hash = str([y, x])
    infected = virus_map[xy_hash]
    if infected:
        face.right()
    else:
        caused_infections += 1
        face.left()
    virus_map[xy_hash] = not infected
    face.move()
print(caused_infections)

