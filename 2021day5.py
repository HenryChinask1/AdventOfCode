import re

lineSegs = open('Advent of Code Inputs/lineSegsTEST.txt').read().split('\n')
coords = []
overlaps = 0
fullOverlaps = 0

# Split the coords in each line seg into the format x1, y1, x2, y2.
for i in lineSegs:
    coords.append(re.split(' -> |,', i))

#print(coords)

# A map of the 
oceanFloor = [[0 for i in range(10)] for _ in range(10)]
oceanFloor2 = [[0 for i in range(10)] for _ in range(10)]

def drawLine(x1, x2, y1, y2):
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            oceanFloor[i][x1] += 1
            oceanFloor2[i][x1] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            oceanFloor[y1][i] += 1
            oceanFloor2[y1][i] += 1
    else:
        for i in range(min(x1, x2), abs(x1 - x2) + 1):
            for j in range(min(y2, y1), abs(y1 - y2) + 1):
                oceanFloor2[j][i] += 1

for i in coords:
    x1 = int(i[0])
    y1 = int(i[1])
    x2 = int(i[2])
    y2 = int(i[3])
    drawLine(x1, x2, y1, y2)
    for i in oceanFloor2:
        print(i)
    print(' ')

for i in oceanFloor:
    for j in i:
        if j > 1:
            overlaps += 1

for i in oceanFloor2:
    for j in i:
        if j > 1:
            fullOverlaps += 1

print(f'Part One: {overlaps}')
print(f'Part Two: {fullOverlaps}')
