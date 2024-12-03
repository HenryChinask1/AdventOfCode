p = open('AdventOfCode/Advent of Code Inputs/2024day2.txt').read().split('\n')

puzzle = []
ans = 0

for i in p:
    puzzle.append([int(i) for i in i.split()])

def listAdj(line):
    n = len(line) - 1
    while n >= 0:
        list1 = line[:]
        list1.pop(n)
        if lineCheck(list1) == 1:
            return 1
        n -= 1
    return 0

def lineCheck(line):
    if line != sorted(line):
        if line != sorted(line, reverse=True):
            return 0
    n = len(line) - 1
    while n:
        if abs(line[n] - line[n - 1]) > 3 or abs(line[n] - line[n -1]) < 1:
            return 0
        n -= 1
    return 1

for line in puzzle:
    if lineCheck(line) == 1:
        ans += 1
    elif listAdj(line) == 1:
        ans += 1

print(ans)