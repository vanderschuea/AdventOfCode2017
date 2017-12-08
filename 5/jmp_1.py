

with open("jmp.txt") as f:
    content = f.readlines()
jumps = [int(x.strip()) for x in content]
ind = 0
count = 0
while 0 <= ind < len(content):
    prev_ind = ind
    ind = ind + jumps[ind]
    jumps[prev_ind] += 1
    count += 1
print(count)
