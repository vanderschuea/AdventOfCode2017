import re

with open("pipes.txt") as f:
    content = f.readlines()
reg = re.compile(r'(\d+) <-> (.+)')
lines = [reg.match(x).groups() for x in content]

problem_length = len(lines)
qu = [x for x in range(problem_length)]
size = [1]*problem_length


def root(x):
    while qu[x] != x:
        x = qu[x]
    return x


for x in lines:
    children = [int(y) for y in x[1].split(", ")]
    r = root(int(x[0]))
    for child in children:
        child_r = root(child)
        if r != child_r:
            if size[child_r] > size[r]:
                qu[r] = child_r
                size[child_r] += size[r]
                r = child_r # the root changed!!
            else:
                qu[child_r] = r
                size[r] += size[child_r]

print(size[root(0)])
