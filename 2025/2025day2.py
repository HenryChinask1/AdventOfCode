import re
ranges = [re.findall(r'\d+', i) for i in open('Advent of Code Inputs/2025day2.txt').read().split(',')]

def checkID(num, part):
    found = re.match(r'\b(\w+)\1+\b', str(num)) if part == 2 else re.match(r'\b(\w+)\1\b', str(num))
    return found

def partOne(ranges):
    ans = sum([sum([(i if checkID(i, 1) else 0) for i in range(int(part[0]), int(part[1]) + 1)]) for part in ranges])
    print(f'Part One: {ans}')

def partTwo(ranges):
    ans = sum([sum([(i if checkID(i, 2) else 0) for i in range(int(part[0]), int(part[1]) + 1)]) for part in ranges])
    print(f'Part Two: {ans}')

partOne(ranges), partTwo(ranges)