def partOne():
    p = open('Advent of Code Inputs/2024day1.txt').read().split('\n')
    leftList = []
    rightList = []

    for i in p:
        leftList.append(i[0:5])
        rightList.append(i[-5:])

    rightList.sort()
    leftList.sort()
    ans = []

    i = 0
    while i < len(leftList):
        ans.append(abs(int(leftList[i]) - int(rightList[i])))
        i += 1

    print(f'2024 Day 1 Part 1: {sum(ans)}')

def partTwo():
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

partOne()
partTwo()