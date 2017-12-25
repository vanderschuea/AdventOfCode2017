from enum import Enum
from collections import defaultdict


# Adapted from day 18
class Type(Enum):
    INT = 0
    STR = 1


def parse(stri):
    arr = stri.strip().split(" ")
    dic = {'action': arr[0]}

    if arr[1].isdigit() or arr[1][1:].isdigit():
        dic['reg'] = [Type.INT, int(arr[1])]
    else:
        dic['reg'] = [Type.STR, arr[1]]

    if len(arr) == 3:
        if arr[2].isdigit() or arr[2][1:].isdigit():
            dic['arg2'] = [Type.INT, int(arr[2])]
        else:
            dic['arg2'] = [Type.STR, arr[2]]
    return dic


with open('coproc.txt') as f:
    content = f.readlines()

instructions = []
for line in content:
    instructions += [parse(line)]

registers = defaultdict(int)
frequencies = []


def value(x):
    if x[0] == Type.INT:
        return x[1]
    else:
        return registers[x[1]]


follow = 0
mul_instructions = 0
while follow < len(instructions):
    instr = instructions[follow]
    ope = instr['action']
    reg = instr['reg']
    if ope == 'set':
        registers[reg[1]] = value(instr['arg2'])
        follow += 1
    elif ope == 'sub':
        registers[reg[1]] -= value(instr['arg2'])
        follow += 1
    elif ope == 'mul':
        registers[reg[1]] *= value(instr['arg2'])
        follow += 1
        mul_instructions += 1
    elif ope == 'jnz':
        if value(reg) != 0:
            follow += value(instr['arg2'])
        else:
            follow += 1

print(mul_instructions)



