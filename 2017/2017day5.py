f = open('Advent of Code Inputs/2017day5.txt').read().split()

def partOne():
    jumps = [int(i) for i in f]
    i = 0
    steps = 0
    while i < len(jumps):
        moveTo = jumps[i]
        jumps[i] += 1
        i += moveTo
        steps += 1       
        
    print(f'Part One: {steps}')

def partTwo():
    jumps = [int(i) for i in f]
    i = 0
    steps = 0
    while i < len(jumps):
        moveTo = jumps[i]
        if moveTo >= 3:
            jumps[i] -= 1
        elif moveTo < 3:
            jumps[i] += 1
        i += moveTo
        steps += 1
        
    print(f'Part Two: {steps}')

partOne()
partTwo()