import sys

with open("sum.txt") as f:
    content = f.readlines()
content = [x.strip().split() for x in content]
checksum = 0
for row in content:
    mn = sys.maxsize
    mx = -sys.maxsize - 1
    for x in row:
        x = int(x)
        if x > mx:
            mx = x
        if x < mn:
            mn = x
    checksum += mx - mn
print(checksum)
