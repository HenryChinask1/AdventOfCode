floorLocator = open('AdventOfCode/Advent of Code Inputs/2015day1.txt').read().strip()

def climb(floorFinder, checkStep=None):
    floor = 0
    step = 0
    
    for i in floorFinder:
        if checkStep:
            if floor == -1:
                print(f'Part Two: {step}')
                return
        if i == '(':
            floor += 1
            step += 1
        elif i == ')':
            floor -= 1
            step += 1
    print(f'Part One: {floor}')
    return

climb(floorLocator)
climb(floorLocator, True)
