from enum import Enum


class State(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


class Tube(Enum):
    SPACE = ' '
    VERTICAL = '|'
    HORIZONTAL = '-'
    CORNER = '+'


def get_offset(state):
    if state == State.UP:
        return [-1, 0]
    elif state == State.DOWN:
        return [1, 0]
    elif state == State.RIGHT:
        return [0, 1]
    elif state == State.LEFT:
        return [0, -1]


with open('pipes.txt') as f:
    content = f.readlines()
network = [list(line[:-1]) for line in content]

# find starting point
point = [0, -1]
for x, i in zip(content[0], range(len(content[0]))):
    if x == '|':
        point[1] = i
        break


direction = State.DOWN
through = []
while True:
    square = network[point[0]][point[1]]
    if square == ' ':
        break
    if square == '+':
        if direction == State.UP or direction == State.DOWN:
            if network[point[0]][point[1]-1] != ' ':
                direction = State.LEFT
            elif len(network[point[0]]) > point[1]+1 and network[point[0]][point[1]+1] != ' ':
                direction = State.RIGHT
            else:
                break
        else:
            if len(network[point[0]-1]) > point[1] and network[point[0]-1][point[1]] != ' ':
                direction = State.UP
            elif len(network) > point[0]+1 and len(network[point[0]+1]) > point[1] and \
                    network[point[0]+1][point[1]] != ' ':
                direction = State.DOWN
            else:
                break
    elif square != '|' and square != '-':
        through += [square]
    next_offset = get_offset(direction)
    point[0] += next_offset[0]
    point[1] += next_offset[1]

print(''.join(through))
