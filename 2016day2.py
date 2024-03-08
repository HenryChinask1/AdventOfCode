movement = open('bathroomcode.txt').read().split('\n')

grid = [['x', 'x', '1', 'x', 'x'],
        ['x', '2', '3', '4', 'x'],
        ['5', '6', '7', '8', '9'],
        ['x', 'A', 'B', 'C', 'x'],
        ['x', 'x', 'D', 'x', 'x']]

currentDirection = (0, 2) # Start at '5'

turns = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

for moves in movement:
    for move in moves:
        newCurrentDirection = (max(0, min(currentDirection[0] + turns[move][0], 4)), max(0, min(currentDirection[1] + turns[move][1], 4)))
        for i in range(50):
            if [newCurrentDirection[1]][newCurrentDirection[0]] != 'x':
                currentDirection = newCurrentDirection
        print(grid[currentDirection[1]][currentDirection[0]])
