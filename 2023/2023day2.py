p = open('AdventOfCode/Advent of Code Inputs/2023day2TEST.txt').read().split('\n')
puzzle = []

for i in p:
    maps = []
    maps.append(i[5:i.index(':')])
    maps.append(i[i.index(':'):i.index(',')].split())
    puzzle.append(maps)

print(puzzle)

def partOne():
    cubes = {'red': 12, 'green': 13, 'blue': 14}


def partTwo():
    pass

partOne()
partTwo()