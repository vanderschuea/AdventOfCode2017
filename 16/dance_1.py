with open('dance.txt') as f:
    dance_moves = f.readlines()[0].split(',')

length = 16

# array to retrieve solution immediately
programs = [chr(c) for c in range(97, 97+length)]

# save a letter's index to have instant specified letter-swaps (p)
indexed = {}
for p, ind in zip(programs, range(length)):
    indexed[p] = ind

# to have instantaneous spins (x)
start_ind = 0

for move in dance_moves:
    if move[0] == 's':
        start_ind = (start_ind - int(move[1:]) + length) % length
    elif move[0] == 'x':
        indices = [(start_ind+int(x)) % length for x in move[1:].split('/')]
        a, b = programs[indices[0]], programs[indices[1]]
        programs[indices[1]], programs[indices[0]] = a, b
        indexed[a], indexed[b] = indexed[b], indexed[a]
    elif move[0] == 'p':
        indices = [indexed[x] for x in move[1:].split('/')]
        a, b = programs[indices[0]], programs[indices[1]]
        programs[indices[1]], programs[indices[0]] = a, b
        indexed[a], indexed[b] = indexed[b], indexed[a]

final = programs[start_ind:] + programs[:start_ind]
print(''.join(final))
