p = open('Advent of Code Inputs/2020day7TEST.txt').read().split('\n')
p = [item.replace('contain', ':') for item in p]
puzzle = []
ans = 0

for i in p:
    for j in range(len(i)):
        if i[j] == ':':
            puzzle.append([i[0:j], i[j + 2:]])

puzzleDict = {i[0]: i[1:] for i in puzzle}

for i in puzzleDict:
    if 'shiny gold bag' in puzzleDict[i][0]:
        ans += 1

print(ans + 1)