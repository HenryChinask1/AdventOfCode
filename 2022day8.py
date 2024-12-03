p = open('AdventOfCode/Advent of Code Inputs/2022day8TEST.txt').read().split('\n')
forest = []

for i in p:
    forest.append([int(j) for j in i])

def checkRow(forest):
    ans = 0
    currMax = 0
    
    for i in range(len(forest[0])):
        if i < currMax:
            break
        else:
            ans += 1
            currMax = max(currMax, i)
    return ans

def checkCol(forest):
    col = 0
    

res = checkRow(forest)

print(res)

