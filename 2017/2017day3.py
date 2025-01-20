puzzle = 347991

def partOne():
    grid = {}
    i = 1
    dx, dy = 0, -1
    row = col = 0
    
    while i <= puzzle:
        grid[i] = [row, col]
        if row == col or (row < 0 and row == -col) or (row > 0 and row == 1 - col):
            dx, dy = -dy, dx
        row, col = row + dx, col + dy
        i += 1

    print(f'Part One: {abs(grid[puzzle][0]) + abs(grid[puzzle][1])}')

def partTwo():
    pass

partOne()
partTwo()