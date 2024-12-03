grid = [[0 for i in range(10000)] for j in range(10000)]
moves = open('Advent of Code Inputs/2019day3.txt').read().split('\n')
start = grid[0][0]
distances = []

for line in moves:
    for move in line:
        grid[line][move] += 1

for col in grid:
    for row in col:
        if grid[row][col] > 1:
            distances.append((abs(row - 500) + abs(col - 500)))


print(max(distances))
