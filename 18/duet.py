from enum import Enum
from collections import defaultdict
from queue import Queue


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


with open('duet.txt') as f:
    content = f.readlines()

instructions = []
for line in content:
    instructions += [parse(line)]


def thread(tid, registers, follow, all_queues, counters):
    def value(x):
        if x[0] == Type.INT:
            return x[1]
        else:
            return registers[x[1]]

    while True:
        instr = instructions[follow]
        ope = instr['action']
        reg = instr['reg']

        if ope == 'snd':
            all_queues[tid].put(value(reg))
            follow += 1
            counters[tid] = [counters[tid][0]+1]
        elif ope == 'rcv':
            if all_queues[not tid].empty():
                return follow  # deadlock
            else:
                registers[reg[1]] = all_queues[not tid].get()
                follow += 1
        elif ope == 'set':
            registers[reg[1]] = value(instr['arg2'])
            follow += 1
        elif ope == 'add':
            registers[reg[1]] += value(instr['arg2'])
            follow += 1
        elif ope == 'mul':
            registers[reg[1]] *= value(instr['arg2'])
            follow += 1
        elif ope == 'mod':
            registers[reg[1]] %= value(instr['arg2'])
            follow += 1
        elif ope == 'jgz':
            if value(reg) > 0:
                follow += value(instr['arg2'])
            else:
                follow += 1


'''
    Context saves which 'thread' is being executed
    queues contains the different buses through which the values are sent
    follows, all_registers contain the different registers and latest 
        instruction_id of each 'thread'
    A deadlock is reached when no value has been sent and it isn't 
        the first iteration
'''
context = 0
follows = [0, 0]
queues = [Queue(), Queue()]
all_registers = [defaultdict(int), defaultdict(int)]
all_registers[1]['p'] = 1
counters = [[0], [0]]
iteration = 0
while True:
    prev = counters[context][0]
    follows[context] = thread(context, all_registers[context],
                              follows[context], queues, counters)
    after = counters[context][0]
    if prev == after and iteration > 0:
        print(counters[1][0])
        break
    context = not context
    iteration += 1




