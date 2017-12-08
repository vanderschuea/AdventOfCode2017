import re


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
    lines[ind] = [x[0], x[1], get_children(x[2])]

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
    dic[x[0]] = x[2]

for x in top:
    top = x
print(top)