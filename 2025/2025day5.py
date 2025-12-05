import re

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
    data = open('Advent of Code Inputs/2025day5.txt').read().split('\n')
    ranges = []
    ans = 0
    fresh = []

    for i in data:
        if '-' in i:
            lowHigh = re.findall(r'\d+', i)
            ranges.append((int(lowHigh[0]), int(lowHigh[1])))
        else:
            break
    ranges.sort()
    prevRange = 0
    #print(ranges)
    for i in range(len(ranges) - 1):
        print(ans)
        if ranges[i][1] > ranges[i + 1][0]:
            ans += ranges[i + 1][0] - ranges[i][0]
            fresh.append([ranges[i + 1][0], ranges[i][0], i, ans])
            prevRange = ranges[i + 1][0] + 1
        elif ranges[i][0] < prevRange:
            ans += ranges[i][1] - prevRange
            fresh.append([ranges[i][1], prevRange, i, ans])
        elif ranges[i][1] == ranges[i + 1][0]:
            ans += ranges[i][1] - ranges[i][0]
        else:
            ans += ranges[i][1] + 1 - ranges[i][0]
            fresh.append([ranges[i][1] + 1, ranges[i][0], i, ans])
    ans += ranges[-1][1] - ranges[-1][0] + 1
    fresh.append([ranges[-1][1], ranges[-1][0], i, ans])
    #print(fresh)
    print(ans)
    print(f'Part Two: {ans}')

partOne()
partTwo()