with open("scanner.txt") as f:
    content = f.readlines()
lines = [[int(y) for y in x.split(": ")] for x in content]
problem_length = lines[len(lines)-1][0] + 1
problem = [0]*problem_length
for line in lines:
    problem[line[0]] = line[1]

total_violation = 5000
start_time = 0
while total_violation > 0:
    violation = 0
    time = start_time
    for x, pos in zip(problem, range(problem_length)):
        if x != 0:
            height = time % (2*x - 2)
            if height == 0:
                violation += 1
                break

        time += 1

    total_violation = violation
    start_time += 1

print(start_time-1)











