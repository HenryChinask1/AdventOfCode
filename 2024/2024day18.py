from collections import deque

p = open('AdventOfCode/Advent of Code Inputs/2024day18.txt').read().split('\n')
puzzle = []

for i in p:
    coords = i.split(',')
    coord = []
    for j in coords:
        coord.append(int(j))
    puzzle.append(coord)

def partOne():
    gridSize = 71
    grid = [['.' for i in range(gridSize)] for i in range(gridSize)]
    for idx, coord in enumerate(puzzle):
        grid[coord[1]][coord[0]] = '#'
        if idx == 1028:
            break

    
    start = (0, 0)
    end = (gridSize - 1, gridSize - 1)
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            print(f'Part One: {len(path) - 1}')
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])

def partTwo():

    def djikstra(grid):
        start = (0, 0)
        end = (gridSize - 1, gridSize - 1)
        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            x, y = path[-1]
            
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(path + [(nx, ny)])
        if end not in visited:
            return True
        return False

    gridSize = 71
    grid = [['.' for i in range(gridSize)] for i in range(gridSize)]
    for idx, coord in enumerate(puzzle):
        grid[coord[1]][coord[0]] = '#'
        if djikstra(grid):
            print(f'Part Two: {coord[0], coord[1]}')
            break

partOne()
partTwo()
