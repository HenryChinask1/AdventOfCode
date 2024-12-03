floorLocator = open('Advent of Code Inputs/2015day1.txt').read().strip()
floor = 0
step = 0

for i in floorLocator:
    if floor == -1:
        break
    if i == '(':
        floor = floor + 1
        step = step + 1
    elif i == ')':
        floor = floor - 1
        step = step + 1

print(step)
