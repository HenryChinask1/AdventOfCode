p = open('Advent of Code Inputs/2024day6.txt').read().split('\n')
puzzle = []

for i in p:
    puzzle.append([j for j in i])


ans = 0
start = (0, 0)

def walkGuard(grid, start, dir):
    pos = start
    dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    prevPos = start
    walking = True
    # Add 'X' until you reach a '#'.
    while walking:
        grid[pos[0]][pos[1]] = 'X'
        prevPos = pos
        pos = tuple(map(lambda i, j: i + j, pos, dirs[dir]))
        if (pos[0] > (len(grid) - 1)) or (pos[1] > (len(grid[0]) - 1)):
            ans = 0
            for row in grid:
                for item in row:
                    if item == 'X':
                        ans += 1
            return ans    
        if grid[pos[0]][pos[1]] == '#':
            walking = False
            if dir == '>':
                dir = 'v'
                walkGuard(grid, prevPos, dir)
            elif dir == 'v':
                dir = '<'
                walkGuard(grid, prevPos, dir)
            elif dir == '<':
                dir = '^'
                walkGuard(grid, prevPos, dir)
            elif dir == '^':
                dir = '>'
                walkGuard(grid, prevPos, dir)
        if (pos[0] > (len(grid) - 1)) or (pos[1] > (len(grid[0]) - 1)):
            ans = 0
            for row in grid:
                for item in row:
                    if item == 'X':
                        ans += 1
            return ans
    ans = 0
    for row in grid:
        for item in row:
            if item == 'X':
                ans += 1
    return ans


# Find the starting point.
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if puzzle[i][j] in '^v><':
            start = (i, j)
            dir = puzzle[i][j]
            puzzle[i][j] ='X'
            # Start the path.
            ans += walkGuard(puzzle, start, dir)

print(f'Part One: {ans}')
