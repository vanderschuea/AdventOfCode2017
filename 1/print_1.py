with open("print.txt") as f:
    c = f.read(1)
    prev = -1
    first = -1
    sm = 0
    while c:
        c = int(c)

        if prev == c:
            sm += c
        if first < 0:
            first = c
        prev = c
        c = f.read(1)
    if first == prev:
        sm += first
    print(sm)

