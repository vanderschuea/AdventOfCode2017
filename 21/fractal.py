from enum import Enum


class Transformation(Enum):
    ROTATE = 1
    FLIP_VERTICAL = 2
    FLIP_HORIZONTAL = 3


def transform(mtr, tr):
    mtr_dim = int(len(mtr) ** 0.5)
    new_mtr = ['.']*len(mtr)

    if tr == Transformation.ROTATE:
        all_mp = [[1, 3, 0, 2],
                  [2, 5, 8, 1, 4, 7, 0, 3, 6]]
    elif tr == Transformation.FLIP_HORIZONTAL:
        all_mp = [[2, 3, 0, 1],
                  [6, 7, 8, 3, 4, 5, 0, 1, 2]]
    else:
        all_mp = [[1, 0, 3, 2],
                  [2, 1, 0, 5, 4, 3, 8, 7, 6]]
    mp = all_mp[mtr_dim - 2]
    for ind in range(len(mtr)):
        new_mtr[mp[ind]] = mtr[ind]

    return new_mtr


with open('fractal.txt') as f:
    content = f.readlines()

all_patterns = {}
for line in content:
    rule = line.strip().split(' => ')
    in_rule = list(''.join(rule[0].split('/')))
    out_rule = list(''.join(rule[1].split('/')))
    # rotations
    for _ in range(4):
        all_patterns[str(in_rule)] = out_rule
        all_patterns[str(transform(in_rule, Transformation.FLIP_HORIZONTAL))] = out_rule
        all_patterns[str(transform(in_rule, Transformation.FLIP_VERTICAL))] = out_rule
        in_rule = transform(in_rule, Transformation.ROTATE)

matrix = ['.', '#', '.', '.', '.', '#', '#', '#', '#']
for _ in range(18):
    size = int(len(matrix) ** 0.5)
    if size % 2 == 0:
        dim = 2
    else:
        dim = 3
    dim1 = dim + 1

    size2 = (size // dim) * dim1
    new_matrix = ['.']*(size2**2)
    for a in range(0, size, dim):
        for b in range(0, size, dim):
            subsample = ['.']*(dim**2)
            for i in range(dim):
                for j in range(dim):
                    subsample[dim*i + j] = matrix[(a+i)*size + b+j]
            new_sample = all_patterns[str(subsample)]
            a2 = (a // dim) * dim1
            b2 = (b // dim) * dim1
            for i in range(dim1):
                for j in range(dim1):
                    new_matrix[(a2+i)*size2 + b2+j] = new_sample[i*dim1+j]
    matrix = new_matrix
total = 0
for x in matrix:
    total += (x == '#')
print(total)
