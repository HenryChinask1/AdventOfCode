import re

data = open('Advent Of Code Inputs/2018day6TEST.txt').read().split('\n')

# Test grid.
grid = [['.'] * 15 for _ in range(15)]
# Max coord is 358, so make the grid 400/400.
#grid = [['.'] * 400 for _ in range(400)]
coords = []
x = 0
for i in data:
    coord = re.findall(r'\d+', i)
    coords.append([int(coord[0]), int(coord[1]), x])
    x += 1

for i in coords:
    grid[i[1]][i[0]] = i[2]

print(grid)