

step = 376
x = 1
ind = 0
after_zero = 0
while x <= 50000000:
    # position where we should insert next value (x = len(buffer))
    ind = ((ind + step) % x) + 1

    if ind == 1:
        after_zero = x
    x += 1
print(after_zero)

