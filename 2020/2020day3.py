import numpy as np


fileInput = open('Advent of Code Inputs/2020day3.txt').read().split('\n')
forest = [[i] for i in fileInput]
bigForest = np.hstack((forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest, forest))
newForest = []
n = 0
trees = 0

for i in bigForest:
    newForest.append(''.join(i))

print(newForest[10])

while n < (len(newForest) - 1):
    for j in range(0, len(newForest[0]), 3):
        #print(n, j)
        if newForest[n][j] == '#':
            trees += 1
            #print(trees)
        n += 1
        if n >= len(newForest):
            break

#print(newForest)

print(trees)
