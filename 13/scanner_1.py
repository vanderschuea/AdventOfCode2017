with open("scanner.txt") as f:
    content = f.readlines()
lines = [[int(y) for y in x.split(": ")] for x in content]
problem_length = lines[len(lines)-1][0] + 1
problem = [0]*problem_length
for line in lines:
    problem[line[0]] = line[1]

violation = 0
time = 0
for x, pos in zip(problem, range(problem_length)):
    if x != 0:
        height = time % (2*x-2)
        if height == 0:
            violation += x*pos

    time += 1

print(violation)











