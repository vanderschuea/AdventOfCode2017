import sys

with open("block.txt") as f:
    content = f.readlines()
blocks = list(map(int, content[0].strip().split()))
dic = {}

max_val = -sys.maxsize - 1
max_ind = -1
for x, ind in zip(blocks, range(len(blocks))):
    if x > max_val:
        max_val = x
        max_ind = ind
count = 0
key = str(blocks)

while key not in dic:
    dic[key] = True

    blocks[max_ind] = 0
    add = max_val // len(blocks)
    max_offset = max_ind + 1 + (max_val % len(blocks))
    offset = max_ind +1
    max_val = 0
    max_ind = -1

    for ind_temp in range(offset, offset + len(blocks)):
        ind = ind_temp % len(blocks)
        if ind_temp < max_offset:
            blocks[ind] += add + 1
        else:
            blocks[ind] += add
        x = blocks[ind]
        if x > max_val or (x == max_val and ind < max_ind):
            max_val = x
            max_ind = ind

    count += 1
    key = str(blocks)
print(count)
