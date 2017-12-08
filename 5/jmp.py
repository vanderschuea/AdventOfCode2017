

with open("jmp.txt") as f:
    content = f.readlines()
jumps = [int(x.strip()) for x in content]
ind = 0
count = 0
while 0 <= ind < len(jumps):
    prev_ind = ind
    jump = jumps[ind]
    ind = ind + jump
    if jump >= 3:
        jumps[prev_ind] -= 1
    else:
        jumps[prev_ind] += 1
    count += 1
print(count)
