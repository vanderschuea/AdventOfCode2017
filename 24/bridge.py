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

    def __str__(self):
        return str(self.a) + '/' +  str(self.b)


with open('bridge.txt') as f:
    content = f.readlines()

pieces = [[int(y) for y in x.split('/')] for x in content]
dominoes = defaultdict(list)

for p in pieces:
    _e = Edge(p[0], p[1])
    dominoes[p[0]] += [_e]
    dominoes[p[1]] += [_e]


def make(node, total, depth):
    max_bridge = total
    max_depth = depth
    for e in dominoes[node]:
        if e.active:
            e.take()
            child = e.other(node)
            new_depth, new_bridge = make(child, total + e.value(), depth+1)
            e.free()
            if new_depth > max_depth or \
                    (new_depth == max_depth and new_bridge > max_bridge):
                max_bridge = new_bridge
                max_depth = new_depth
    return max_depth, max_bridge


print(make(0, 0, 0))
