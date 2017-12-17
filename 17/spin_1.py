buffer = [0]
step = 376
ind = 0
x = 1
while x < 2018:
    ind = ((ind + step) % len(buffer)) + 1
    buffer = buffer[0:ind] + [x] + buffer[ind:]
    x += 1

for x, i in zip(buffer, range(len(buffer))):
    if x == 2017:
        print(buffer[i+1])
        break

