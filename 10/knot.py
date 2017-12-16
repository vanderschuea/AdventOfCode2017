with open("knot.txt") as f:
    lengths = []
    c = f.read(1)
    while c:
        lengths += [ord(c)]
        c = f.read(1)
lengths += [17, 31, 73, 47, 23]

curr = 0
skip = 0
tab = [x for x in range(256)]
for _ in range(64):
    for le in lengths:
        # Reversing
        for i in range(le//2):
            s1 = (curr+i) % 256
            s2 = (curr+le-1-i) % 256
            tab[s1], tab[s2] = tab[s2], tab[s1]

        # Moving forward
        curr = (curr + le+skip) % 256

        # Increase Skip
        skip += 1

final_str = ""
for i in range(16):
    offset = i*16
    xor = tab[offset]
    for j in range(offset+1, offset+16):
        xor ^= tab[j]

    def to_form(s):
        if len(s) == 3:
            return "0"+s[2]
        else:
            return s[2:4]

    final_str += '{:02x}'.format(xor)

print(final_str)
