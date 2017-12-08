import re
import sys

def get_children(str):
    if str:
        str2 = str[4:]
        return str2.split(', ')
    return None


with open("tree.txt") as f:
    content = f.readlines()
reg = re.compile(r'(\w+) \((\d+)\)( -> (\w+(, )?)+)?')

lines = [reg.match(x).groups() for x in content]
for x, ind in zip(lines, range(len(lines))):
    lines[ind] = [x[0], int(x[1]), get_children(x[2])]

dic = {}
top = {}
for x in lines:
    if x[0] not in dic:
        top[x[0]] = True
    if x[2]:
        for y in x[2]:
            if y in top:
                del top[y]
            if y not in dic:
                dic[y] = None
    dic[x[0]] = [x[1], x[2]]

for x in top:
    top = x


def rebalance(sons, y, val):
    count = 0
    for v in y:
        if v == val:
            count +=1
    if count == 1:
        val = y[0]
    for v, son in zip(y, sons):
        if v != val:
            x = dic[son]
            print(val - (v - x[0]))


def check_balance(root):
    x = dic[root]
    if not x[1]:
        return x[0]
    else:
        y = []
        for son in x[1]:
            y += [check_balance(son)]
        val = -1
        for son in y:
            if val != -1 and val != son:
                rebalance(x[1], y, son)
                sys.exit(0)
            val = son
        return x[0]+len(y)*val


check_balance(top)
