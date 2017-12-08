with open("print.txt") as f:
    c = f.read(1)
    ln = []
    while c:
        ln += [int(c)]
        c = f.read(1)

    sm = 0
    offset = len(ln)//2
    for c, ind in zip(ln, range(len(ln))):
        if ln[(ind+offset) % len(ln)] == c:
            sm += c
    print(sm)

