import re

p = open('AdventOfCode/Advent of Code Inputs/2024day14TEST.txt').read().split('/n')
parse = []
puzzle = []

for i in p:
    parse.append(i.split('\n'))

for i in parse[0]:
    puzzle.append(i)

def partOne():
    def parseRobot(robot):
        robotVals = re.findall(r'-?\d+', robot)
        pos = (int(robotVals[0]), int(robotVals[1]))
        vels = (int(robotVals[2]), int(robotVals[3]))
        return [pos, vels]

    grid = {(j, i): 0 for i in range(11) for j in range(7)}
    print(grid)
    robots = []
    for i in puzzle:
        robots.append(parseRobot(i))
    #drop in robots at start.
    for i in robots:
        grid[(i[0][1], i[0][0])] += 1
    print(sum(grid.values()))
    

def partTwo():
    pass

partOne()
partTwo()