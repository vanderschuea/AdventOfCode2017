from math import *
import argparse


def get_ij(case):
    rim = int(ceil(sqrt(case)))
    if rim == 1:
        return 0, 0
    elif (rim % 2) == 0:
        rim += 1
    corner = rim*rim-(rim-1)
    for itr in range(4):
        if case > corner:
            middle = corner+rim//2
            mx = (rim-1)//2
            va = case-middle
            if itr == 0:
                i = -mx
                j = va
            elif itr == 1:
                i = -va
                j = -mx
            elif itr == 2:
                i = mx
                j = -va
            else:  # if itr == 3:
                i = va
                j = mx
            return i, j
        corner -= rim-1
    return None


def calc(case):
    last = 0
    ind = 2
    dic = {str([0, 0]): 1}
    while last <= case:
        i, j = get_ij(ind)
        new = 0
        for di, dj in zip([1, 1, 1, 0, 0, -1, -1, -1],
                          [-1, 0, 1, -1, 1, -1, 0, 1]):
            ni, nj = i+di, j+dj
            key = str([ni, nj])
            if key in dic:
                new += dic[key]

        dic[str([i, j])] = new
        last = new
        ind += 1
    return last


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('case', metavar='N', type=int, nargs=1,
                    help='input')
p = parser.parse_args()
print(calc(p.case[0]))
