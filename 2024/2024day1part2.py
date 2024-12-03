p = open('AdventOfCode/Advent of Code Inputs/2024day1.txt').read().split('\n')

leftList = []
rightList = []
ans = []

for i in p:
    leftList.append(i[0:5])
    rightList.append(i[-5:])

for i in leftList:
    ans.append(int(i) * rightList.count(str(i)))

print(f'2024 Day 1 Part 2: {sum(ans)}')