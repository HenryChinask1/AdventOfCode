movement = open('Advent of Code Inputs/2016day2.txt').read().split('\n')

grid = [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]

startPos = (1, 1) # Start at '5'

turns = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

for moves in movement:
    for move in moves:
        currDir = (max(0, min(startPos[0] + turns[move][0], 2)), max(0, min(startPos[1] + turns[move][1], 2)))
        startPos = currDir
    print(grid[currDir[0]][currDir[1]])