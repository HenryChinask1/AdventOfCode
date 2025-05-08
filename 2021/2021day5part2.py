import re

lineSegs = open('AdventOfCode/Advent of Code Inputs/2021day5TEST.txt').read().split('\n')
coords = []
fullOverlaps = 0

# Split the coords in each line seg into the format x1, y1, x2, y2.
for i in lineSegs:
    coords.append((re.split(' -> |,', i)))

oceanFloor = [[0 for i in range(10)] for _ in range(10)]

def drawLine(x1, x2, y1, y2, ocean):
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            ocean[i][x1] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            ocean[y1][i] += 1
    elif x1 > x2 and y1 > y2:
        startx = x1
        starty = y1
        ocean[startx][starty] += 1
        while startx > x2:
            ocean[startx - 1][starty - 1] += 1
            startx -= 1
            starty -= 1
    elif x1 < x2 and y1 < y2:
        startx = x1
        starty = y1
        ocean[startx][starty] += 1
        while startx < x2:
            ocean[startx + 1][starty + 1] += 1
            startx += 1
            starty += 1
    elif x1 > x2 and y1 < y2:
        startx = x1
        starty = y1
        ocean[startx][starty] += 1
        while startx < x2:
            ocean[startx + 1][starty - 1] += 1
            startx += 1
            starty -= 1
    elif x1 < x2 and y1 > y2:
        startx = x1
        starty = y1
        ocean[startx][starty] += 1
        while startx > x2:
            ocean[startx - 1][starty + 1] += 1
            startx -= 1
            starty += 1
    return ocean

for i in coords:
    x1, y1, x2, y2 = [int(x) for x in i]
    oceanFloor = drawLine(x1, x2, y1, y2, oceanFloor)
    print(oceanFloor)

for i in oceanFloor:
    for j in i:
        if j > 1:
            fullOverlaps += 1

print(f'Part Two: {fullOverlaps}')
    
    