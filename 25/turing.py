from enum import Enum
from collections import defaultdict

class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5


ind = 0
iterator = 0
band = defaultdict(bool)
state = State.A
while iterator < 12208951:
    val = band[ind]
    if state == State.A:
        if not val:
            band[ind] = True
            ind += 1
            state = State.B
        else:
            band[ind] = False
            ind -= 1
            state = State.E
    elif state == State.B:
        if not val:
            band[ind] = True
            ind -= 1
            state = State.C
        else:
            band[ind] = False
            ind += 1
            state = State.A
    elif state == State.C:
        if not val:
            band[ind] = True
            ind -= 1
            state = State.D
        else:
            band[ind] = False
            ind += 1
            state = State.C
    elif state == State.D:
        if not val:
            band[ind] = True
            ind -= 1
            state = State.E
        else:
            band[ind] = False
            ind -= 1
            state = State.F
    elif state == State.E:
        if not val:
            band[ind] = True
            ind -= 1
            state = State.A
        else:
            band[ind] = True
            ind -= 1
            state = State.C
    elif state == State.F:
        if not val:
            band[ind] = True
            ind -= 1
            state = State.E
        else:
            band[ind] = True
            ind += 1
            state = State.A
    iterator += 1

total = 0
for x in band:
    total += band[x]
print(total)
