movement = open('2016day2.txt').read().split('\n')

grid = [['x', 'x', '1', 'x', 'x'],
        ['x', '2', '3', '4', 'x'],
        ['5', '6', '7', '8', '9'],
        ['x', 'A', 'B', 'C', 'x'],
        ['x', 'x', 'D', 'x', 'x']]

allowedCoords = [(0, 2), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (4, 2)]

startPos = (2, 0) # Start at '5'

turns = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

for moves in movement:
    for move in moves:
        currDir = (max(0, min(startPos[0] + turns[move][0], 4)), max(0, min(startPos[1] + turns[move][1], 4)))
        if grid[currDir[0]][currDir[1]] != 'x':
            startPos = currDir
    print(grid[startPos[0]][startPos[1]])