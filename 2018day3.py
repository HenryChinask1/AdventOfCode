file = open('Advent of Code Inputs/2018day3.txt').read().split('\n')
quilt = [[0] * 1000 for _ in range(1000)] # The empty grid.
squares = [] # The list of claims.
ans = 0

for i in file:
    squares.append(i.split(' '))

def startPos(gridStart):
    gridStart = gridStart[0:-1].split(',')
    return((int(gridStart[0]), int(gridStart[1])))

def patchSize(quiltSize):
    quiltSize = quiltSize.split('x')
    return((int(quiltSize[0]),int(quiltSize[1])))


for id, symbol, gridStart, quiltSize in squares:
    start = startPos(gridStart)
    size = patchSize(quiltSize)
    for col in range(start[1], start[1] + size[1]):
        for row in range(start[0], start[0] + size[0]):
            quilt[row][col] += 1

for line in quilt:
    for inch in line:
        if inch > 1:
            ans += 1

for id, symbol, gridStart, quiltSize in squares:
    start = startPos(gridStart)
    size = patchSize(quiltSize)
    total = 0
    for col in range(start[1], start[1] + size[1]):
        for row in range(start[0], start[0] + size[0]):
            total += quilt[row][col]
    if total == size[0] * size[1]:
        print(f'Part 2: {id}')
            
        
#print(quilt)
print(f'Part 1: {ans}')