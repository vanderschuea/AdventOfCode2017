with open("knot.txt") as f:
    content = f.readlines()
lengths =[int(x) for x in content[0].split(',')]

curr = 0
skip = 0
tab = [x for x in range(0, 256)]
for le in lengths:
    # Reversing
    for i in range(0, le//2):
        s1 = (curr+i) % 256
        s2 = (curr+le-1-i) % 256
        tab[s1], tab[s2] = tab[s2], tab[s1]

    # Moving forward
    curr = (curr+le+skip) % 256

    # Increase Skip
    skip += 1

print(tab[0]*tab[1])