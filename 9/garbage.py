from enum import Enum


class State(Enum):
    TAKING = 1
    IGNORE = 2
    GARBAGE = 3


with open('garbage.txt') as f:
    c = f.read(1)
    non_canceled = 0
    state = State.TAKING
    previous_state = state
    while c:
        if c == '!' and not state == State.IGNORE:
            previous_state = state
            state = state.IGNORE
        elif state == State.TAKING:
            if c == '{':
                pass
            elif c == '}':
                pass
            elif c == '<':
                state = state.GARBAGE
        elif state == State.IGNORE:
            state = previous_state
        elif state == State.GARBAGE:
            if c == '>':
                state = State.TAKING
            else:
                non_canceled += 1
        c = f.read(1)
print(non_canceled)
