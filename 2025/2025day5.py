import re
from collections import Counter

def partOne():
    data = open('Advent of Code Inputs/2025day5.txt').read().split('\n')
    ranges = []
    ingredients = []
    ans = 0

    for i in data:
        if '-' in i:
            lowHigh = re.findall(r'\d+', i)
            ranges.append((int(lowHigh[0]), int(lowHigh[1])))
        elif i == '':
            pass
        else:
            ingredients.append(int(i))
    
    for ingredient in sorted(ingredients):
        for nums in sorted(ranges):
            if ingredient < nums[0] or ingredient > nums[1]:
                continue
            elif ingredient >= nums[0] and ingredient <= nums[1]:
                ans += 1
                break
    print(f'Part One: {ans}')

def partTwo():
    data = open('Advent of Code Inputs/2025day5TEST.txt').read().split('\n')
    ranges = []
    ans = []
    # minRange = 10000000000000007
    # maxRange = 0

    for i in data:
        if '-' in i:
            lowHigh = re.findall(r'\d+', i)
            if int(lowHigh[0]) > int(lowHigh[1]):
                ranges.append((int(lowHigh[1]), int(lowHigh[0])))
                # minRange = min(minRange, int(lowHigh[1]))
                # maxRange = max(maxRange, int(lowHigh[0]))
            else:
                ranges.append((int(lowHigh[0]), int(lowHigh[1])))
                # minRange = min(minRange, int(lowHigh[0]))
                # maxRange = max(maxRange, int(lowHigh[1]))
        else:
            break

    ranges.sort()
    lowBound = ranges[0][0]
    highBound = ranges[0][1]
    for i in range(len(ranges) - 1):
        print(lowBound, highBound, ans)
        if ranges[i][0] >= lowBound and ranges[i][0] > highBound:
            ans.append(highBound - lowBound)
            lowBound = ranges[i][0]
        elif ranges[i][0] >= lowBound and ranges[i][0] <= highBound:
            if ranges[i][1] > highBound:
                highBound = ranges[i][1]
        if ranges[i][1] <= lowBound:
            if ranges[i + 1][0] > highBound:
                ans.append(highBound - lowBound)
                lowBound = ranges[i + 1][0]

        elif ranges[i][0] >= lowBound and ranges[i][1] <= highBound:
                continue

    print(f'Part Two: {sum(ans)}')

partOne()
partTwo()