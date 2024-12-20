p = open('AdventOfCode/Advent of Code Inputs/2024day10TEST.txt').read().split('\n')
puzzle = [] # A grid.

for i in p:
    puzzle.append([int(num) for num in i])
print(puzzle)

def partOne():
    ans = 0

    def checkPath(puzzle, row, col):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        start = [row, col]
        currHeight = 9
        currChecks = []
        while currHeight == currHeight or currHeight == currHeight - 1:
            for direction in dirs:
                currChecks.append([start[0] + direction[0], start[1] + direction[1]])
                if puzzle[start[0] + direction[0]][start[1] + direction[1]] == currHeight - 1:
                    start[0] += direction[0] 
                    start[1] += direction[1]
                    currHeight -= 1
                    if currHeight < 0:
                        return 1
                if len(currChecks) == 4:
                    return 0
        return 0

    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == 9:
                ans += checkPath(puzzle, row, col)
    print(f'Part One: {ans}')

def partTwo():
    pass

partOne()
partTwo()

