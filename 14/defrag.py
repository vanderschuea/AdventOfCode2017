# see week 10
def knot_hash(input):
    lengths = []
    for c in input:
        lengths += [ord(c)]
    lengths += [17, 31, 73, 47, 23]

    curr = 0
    skip = 0
    tab = [x for x in range(256)]
    for _ in range(64):
        for le in lengths:
            # Reversing
            for i in range(le // 2):
                s1 = (curr + i) % 256
                s2 = (curr + le - 1 - i) % 256
                tab[s1], tab[s2] = tab[s2], tab[s1]

            # Moving forward
            curr = (curr + le + skip) % 256

            # Increase Skip
            skip += 1

    final_str = ""
    for i in range(16):
        offset = i * 16
        xor = tab[offset]
        for j in range(offset + 1, offset + 16):
            xor ^= tab[j]

        def to_form(s):
            if len(s) == 3:
                return "0" + s[2]
            else:
                return s[2:4]

        final_str += '{:08b}'.format(xor)

    return final_str


phrase = 'jxqlasbh-'
disk_map = [[0]*128 for _ in range(128)]
tot_region = 0
root_dic = {}


def root(x):
    while root_dic[x] != x:
        x = root_dic[x]
    return x


for i in range(128):
    for c, j in zip(knot_hash(phrase + str(i)), range(128)):
        if int(c):
            region_number = i*128 + j + 1  # offset of one to avoid 0's
            i_cond = i != 0 and disk_map[i-1][j]
            j_cond = j != 0 and disk_map[i][j-1]

            if i_cond and j_cond:
                r1 = root(disk_map[i-1][j])
                r2 = root(disk_map[i][j-1])
                root_dic[region_number] = r1
                if r1 != r2:
                    root_dic[r2] = r1
                    tot_region -= 1
            elif i_cond:
                r = root(disk_map[i-1][j])
                root_dic[region_number] = r
            elif j_cond:
                r = root(disk_map[i][j-1])
                root_dic[region_number] = r
            else:
                root_dic[region_number] = region_number
                tot_region += 1
            disk_map[i][j] = region_number

print(tot_region)


