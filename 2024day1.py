p = open('AdventOfCode/Advent of Code Inputs/2024day1.txt').read().split('\n')
leftList = []
rightList = []

for i in p:
    leftList.append(i[0:5])
    rightList.append(i[-5:])

print(leftList, rightList)
rightList.sort()
leftList.sort()
ans = []

i = 0
while i < len(leftList):
    ans.append(abs(int(leftList[i]) - int(rightList[i])))
    i += 1

print(sum(ans))