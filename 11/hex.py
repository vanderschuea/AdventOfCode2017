from collections import defaultdict

with open("hex.txt") as f:
    content = f.readlines()
directions = [x for x in content[0].split(',')]

dic = defaultdict(int)
x, y = 0, 0
mx = 0
for d in directions:
    if d == 'n':
        y += 1
    elif d == 's':
        y -= 1
    elif d == 'ne':
        y += 0.5
        x += 1
    elif d == 'nw':
        y += 0.5
        x -= 1
    elif d == 'se':
        y -= 0.5
        x += 1
    elif d == 'sw':
        y -= 0.5
        x -= 1
    dist = abs(x) + abs(y) - abs(x)//2
    mx = max(mx, dist)

print(mx)

