p = open('AdventOfCode/Advent of Code Inputs/2024day2.txt').read().split('\n')

puzzle = []
ans = 0

for i in p:
    puzzle.append([int(i) for i in i.split()])

def lineCheck(line, inc=False):
    if inc:
        if line != sorted(line):
            return 0
    if not inc:
        if line != sorted(line, reverse=True):
            return 0
    for i in range(len(line) - 1):
        if abs(line[i] - line[i + 1]) >= 4 or abs(line[i] - line[i + 1]) <= 0:
            return 0
    return 1

for line in puzzle:
    if line[1] > line[0]:
        ans += lineCheck(line, inc=True)
    else:
        ans += lineCheck(line, inc=False)

print(ans)