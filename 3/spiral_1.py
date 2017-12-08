from math import *
import argparse

case2 = 361527


def get_ij(case):
    rim = int(ceil(sqrt(case)))
    if rim == 1:
        return 0, 0
    if (rim % 2) == 0:
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


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('case', metavar='N', type=int, nargs=1,
                    help='input')
p = parser.parse_args()
i, j = get_ij(p.case[0])
print(abs(i)+abs(j))
