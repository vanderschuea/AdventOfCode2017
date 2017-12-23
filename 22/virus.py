from collections import defaultdict
from enum import EnumMeta, IntEnum


class DefaultEnumMeta(EnumMeta):
    default = object()

    def __call__(cls, value=default, *args, **kwargs):
        if value is DefaultEnumMeta.default:
            # Assume the first enum is default
            return next(iter(cls))
        return super().__call__(value, *args, **kwargs)


class State(IntEnum, metaclass=DefaultEnumMeta):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


class Face:
    def __init__(self, _x, _y):
        self.dir = [0, -1]
        self.x = _x
        self.y = _y

    def left(self):
        d = self.dir
        if d == [0, -1]: self.dir = [-1, 0]
        elif d == [0, 1]: self.dir = [1, 0]
        elif d == [-1, 0]: self.dir = [0, 1]
        elif d == [1, 0]: self.dir = [0, -1]

    def right(self):
        self.left()
        self.reverse()

    def reverse(self):
        self.dir = [-self.dir[0], -self.dir[1]]

    def move(self):
        self.x += self.dir[1]
        self.y += self.dir[0]


with open('virus.txt') as f:
    content = f.readlines()
temp_map = [list(line.strip()) for line in content]
virus_map = defaultdict(State)
for y in range(len(temp_map)):
    for x in range(len(temp_map[0])):
        if temp_map[y][x] == '#':
            virus_map[str([x, y])] = State.INFECTED
face = Face(len(temp_map)//2, len(temp_map[0])//2)

caused_infections = 0
for _ in range(10000000):
    x, y = face.x, face.y
    xy_hash = str([y, x])
    state = virus_map[xy_hash]
    if state == State.CLEAN:
        face.left()
        virus_map[xy_hash] = State.WEAKENED
    elif state == State.WEAKENED:
        virus_map[xy_hash] = State.INFECTED
        caused_infections += 1
    elif state == State.INFECTED:
        face.right()
        virus_map[xy_hash] = State.FLAGGED
    elif state == State.FLAGGED:
        face.reverse()
        virus_map[xy_hash] = State.CLEAN

    face.move()
print(caused_infections)

