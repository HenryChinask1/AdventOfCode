import re

p = open('AdventOfCode/Advent of Code Inputs/2017day7.txt').read().split('\n')

# Parse input.
tower = {}
for i in p:
    lines = re.findall(r'[a-z]+|[0-9]+', i)
    name, wgt = lines[0], lines[1]
    children = []
    if len(lines) > 2:
        for i in lines[2:]:
            children.append(i)
    tower[name] = {'weight': int(wgt), 'children': children}

# Add all the children to a set.
allChildren = set()
for program in tower.values():
    allChildren.update(program['children'])

# Check which program in the tower is at the bottom.
for program in tower:
    if program not in allChildren:
        print(program)