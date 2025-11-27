# Wire Crossings

def partOne():

    def parseInput():
        p = open('Advent of Code Inputs/2019day3.txt').read().split('\n')
        puzzle = []
        for i in p:
            puzzle.append([i.split(',')])
        wireOne = []
        wireTwo = []

        for wire in puzzle[0][0]:
            wireOne.append([wire[0], wire[1:]])
        for wire in puzzle[1][0]:
            wireTwo.append([wire[0], wire[1:]])
        return wireOne, wireTwo
    
    def addWire(piece, points):
        currPos = [0, 0]
        for i in piece:
            currDir = i[0]
            if currDir == 'L':
                end = currPos[1] - int(i[1])
                while currPos[1] > end:
                    currPos = [currPos[0], currPos[1] - 1]
                    if (currPos[0], currPos[1]) not in points:
                        points[currPos[0], currPos[1]] = 1
                    else:
                        points[currPos[0], currPos[1]] += 1
            elif currDir == 'R':
                end = currPos[1] + int(i[1])
                while currPos[1] < end:
                    currPos = [currPos[0], currPos[1] + 1]
                    if (currPos[0], currPos[1]) not in points:
                        points[currPos[0], currPos[1]] = 1
                    else:
                        points[currPos[0], currPos[1]] += 1
            elif currDir == 'U':
                end = currPos[0] - int(i[1])
                while currPos[0] > end:
                    currPos = [currPos[0] - 1, currPos[1]]
                    if (currPos[0], currPos[1]) not in points:
                        points[currPos[0], currPos[1]] = 1
                    else:
                        points[currPos[0], currPos[1]] += 1
            elif currDir == 'D':
                end = currPos[0] + int(i[1])
                while currPos[0] < end:
                    currPos = [currPos[0] + 1, currPos[1]]
                    if (currPos[0], currPos[1]) not in points:
                        points[currPos[0], currPos[1]] = 1
                    else:
                        points[currPos[0], currPos[1]] += 1
        return points
    
    first, second = parseInput()
    gridOne = {}
    gridTwo = {}
    gridOne = addWire(first, gridOne)
    gridTwo = addWire(second, gridTwo)
    crosses = list(filter(lambda x: x in gridOne, gridTwo))
    
    ans = []

    for i in crosses:
        ans.append(abs(0 - i[0]) + abs(0 - i[1]))

    print(f'Part One: {min(ans)}')

def partTwo():

    def parseInput():
        p = open('AdventOfCode/Advent of Code Inputs/2019day3.txt').read().split('\n')
        puzzle = []
        for i in p:
            puzzle.append([i.split(',')])
        wireOne = []
        wireTwo = []

        for wire in puzzle[0][0]:
            wireOne.append([wire[0], wire[1:]])
        for wire in puzzle[1][0]:
            wireTwo.append([wire[0], wire[1:]])
        return wireOne, wireTwo
    
    def addWire(piece):
        points = []
        currPos = [0, 0]
        for i in piece:
            currDir = i[0]
            if currDir == 'L':
                end = currPos[1] - int(i[1])
                while currPos[1] > end:
                    currPos = [currPos[0], currPos[1] - 1]
                    points.append([currPos[0], currPos[1]])
            elif currDir == 'R':
                end = currPos[1] + int(i[1])
                while currPos[1] < end:
                    currPos = [currPos[0], currPos[1] + 1]
                    points.append([currPos[0], currPos[1]])
            elif currDir == 'U':
                end = currPos[0] - int(i[1])
                while currPos[0] > end:
                    currPos = [currPos[0] - 1, currPos[1]]
                    points.append([currPos[0], currPos[1]])
            elif currDir == 'D':
                end = currPos[0] + int(i[1])
                while currPos[0] < end:
                    currPos = [currPos[0] + 1, currPos[1]]
                    points.append([currPos[0], currPos[1]])
        return points
    
    first, second = parseInput()
    gridOne = addWire(first)
    gridTwo = addWire(second)

    res = []

    for i in range(len(gridOne)):
        if gridOne[i] in gridTwo:
            res.append(len(gridOne[0:i + 1]) + len(gridTwo[0:gridTwo.index(gridOne[i]) + 1]))

    print(f'Part Two: {min(res)}')

partOne()
partTwo()