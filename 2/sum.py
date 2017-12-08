import sys

with open("sum.txt") as f:
    content = f.readlines()
content = [map(int, x.strip().split()) for x in content]

checksum = 0
for row in content:
    mn = sys.maxsize
    mx = -sys.maxsize - 1
    ok = False
    for i in range(len(row)):
        for j in range(i+1, len(row)):
            x = row[i]
            y = row[j]
            if x < y:
                x, y = y, x
            if x % y == 0:
                checksum += x//y
                ok = True
                break
        if ok:
            break
print(checksum)
