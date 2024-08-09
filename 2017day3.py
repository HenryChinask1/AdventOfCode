puzzle = 347991

grid = [[0 for i in range(puzzle)] for i in range(puzzle)]
dirs = [[0, 1], [-1, 0], [0, 1], [1, 0]]
step = 1
direction = 0
rStart = int(puzzle / 2)
cStart = int(puzzle / 2)
startPos = (0, 0)

for i in range(1, puzzle):
    for _ in range(3):
        for _ in range(step):
            if(rStart >= 0 and rStart < puzzle and cStart >= 0 and cStart < puzzle):
                grid[rStart][cStart] = i
                rStart += dirs[direction][0]
                cStart += dirs[direction][1]
        direction = (direction + 1) % 4
    step += 1

print(grid)