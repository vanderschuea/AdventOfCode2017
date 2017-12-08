import re
import sys
from collections import defaultdict

with open("instr.txt") as f:
    content = f.readlines()
reg = re.compile(r'(\w+) (inc|dec) (-?\d+) '
                 r'if (\w+) (<|>|==|!=|<=|>=) (-?\d+)')

dic = defaultdict(int)
lines = [reg.match(x).groups() for x in content]

for l in lines:
    if l[4] == '<':
        cond = dic[l[3]] < int(l[5])
    elif l[4] == '<=':
        cond = dic[l[3]] <= int(l[5])
    elif l[4] == '>':
        cond = dic[l[3]] > int(l[5])
    elif l[4] == '>=':
        cond = dic[l[3]] >= int(l[5])
    elif l[4] == '==':
        cond = dic[l[3]] == int(l[5])
    else:  # l[4] == '!=':
        cond = dic[l[3]] != int(l[5])

    if cond:
        if l[1] == 'inc':
            dic[l[0]] += int(l[2])
        else:  # if l[1] == 'dec':
            dic[l[0]] -= int(l[2])

mx = -sys.maxsize - 1
for x in dic:
    if dic[x] > mx:
        mx = dic[x]
print(mx)
