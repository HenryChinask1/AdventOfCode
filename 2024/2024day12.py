p = open('AdventOfCode/Advent oF Code Inputs/2024day12.txt').read().split('\n')
puzzle = []
for i in p:
    puzzle.append([l for l in i])

def isValid(p, maxX, maxY):
    x, y = p
    return 0 <= x < maxX and 0 <= y < maxY

def floodFill(grid, p):
    maxX, maxY = len(grid[0]), len(grid)

    startX, startY = p
    crop = grid[startY][startX]

    visited = set()
    toVisit = [p]

    while toVisit:
        x, y = toVisit.pop()
        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if isValid((nx, ny), maxX, maxY) and grid[ny][nx] == crop and (nx, ny) not in visited:
                toVisit.append((nx, ny))
    return visited

def perimeter(points):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return sum((p[0] + dx, p[1] + dy) not in points for p in points for dx, dy in deltas)

def partOne():
    crops = []
    visited = set()
    for y, line in enumerate(puzzle):
        for x, letter in enumerate(line):
            if (x, y) not in visited and letter not in crops:
                v = floodFill(puzzle, (x, y))
                crops.append(v)
                visited |= v
    print(sum(len(v) * perimeter(v) for v in crops))

def partTwo():
    pass

partOne()
partTwo()
