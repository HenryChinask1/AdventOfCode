import re

def partOne():
    data = open('Advent of Code Inputs/2025day2.txt').read().split(',')
    ranges = []
    ans = 0

    def checkID(num):
        found = re.match(r'\b(\w+)\1\b', str(num))
        if found:
            return True
        return False

    for i in data:
        ranges.append(re.findall(r'\d+', i))
    
    for part in ranges:
        for i in range(int(part[0]), int(part[1]) + 1):
            if checkID(i):
                ans += i
    print(f'Part One: {ans}')

def partTwo():
    data = open('Advent of Code Inputs/2025day2.txt').read().split(',')
    ranges = []
    ans = 0

    def checkID(num):
        found = re.match(r'\b(\w+)\1+\b', str(num))
        if found:
            return True
        return False

    for i in data:
        ranges.append(re.findall(r'\d+', i))
    
    for part in ranges:
        for i in range(int(part[0]), int(part[1]) + 1):
            if checkID(i):
                ans += i
    print(f'Part Two: {ans}')

partOne()
partTwo()