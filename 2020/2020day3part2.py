import numpy as np



# Get data.
fileInput = open('Advent of Code Inputs/2020day3.txt').read().split('\n')
forest = [[i] for i in fileInput]
# Stack the list to the right.
bigForest = np.hstack((forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest))
# Make the list accessible by coordinates.
newForest = []
for i in bigForest:
    newForest.append(''.join(i))

# Check for trees based on slope givem.
def treesOnSlope(newForest, n, xIncrement, yIncrement):
    trees = 0
    while n < (len(newForest) - 1):
        for j in range(0, len(newForest[0]), xIncrement):
            #print(n, j)
            if newForest[n][j] == '#':
                trees += 1
                #print(n, j)
            n += yIncrement
            if n >= len(newForest):
                break
    return trees

ans = treesOnSlope(newForest, 0, 1, 1) * treesOnSlope(newForest, 0, 3, 1) * treesOnSlope(newForest, 0, 5, 1) * treesOnSlope(newForest, 0, 7, 1) * treesOnSlope(newForest, 0, 1, 2)

print(ans)
# print(treesOnSlope(newForest, 0, 1, 1))
# print(treesOnSlope(newForest, 0, 3, 1))
# print(treesOnSlope(newForest, 0, 5, 1))
# print(treesOnSlope(newForest, 0, 7, 1))
# print(treesOnSlope(newForest, 0, 1, 2))