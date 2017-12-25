from collections import defaultdict


class Edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.active = True

    def other(self, x):
        if self.a == x:
            return self.b
        else:
            return self.a

    def value(self):
        return self.a + self.b

    def take(self):
        self.active = False

    def free(self):
        self.active = True


with open('bridge.txt') as f:
    content = f.readlines()

pieces = [[int(y) for y in x.split('/')] for x in content]
dominoes = defaultdict(list)

for p in pieces:
    _e = Edge(p[0], p[1])
    dominoes[p[0]] += [_e]
    dominoes[p[1]] += [_e]


def make(node, total):
    max_bridge = total
    for e in dominoes[node]:
        if e.active:
            e.take()
            child = e.other(node)
            new_bridge = make(child, total + e.value())
            e.free()
            if new_bridge > max_bridge:
                max_bridge = new_bridge
    return max_bridge


print(make(0, 0))
