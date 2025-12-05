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

    for i in data:
        if '-' in i:
            lowHigh = re.findall(r'\d+', i)
            ranges.append((int(lowHigh[0]), int(lowHigh[1])))
        else:
            break
    ranges.sort()

    for i in range(len(ranges) - 1):
        ans += ranges[i][1] - ranges[i][0] + 1
        if ranges[i][1] - ranges[i + 1][0] > 0:
            ans -= ranges[i][1] - ranges[i + 1][0] + 1
    ans += ranges[-1][1] - ranges[-1][0] + 1
    print(f'Part Two: {ans}')

partOne()
partTwo()