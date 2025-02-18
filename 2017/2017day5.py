f = open('AdventOfCode/Advent of Code Inputs/2017day5TEST.txt').read().split()
jumps = [int(i) for i in f]

def partOne():

    i = 0
    steps = 0
    while i < len(jumps):
        moveTo = jumps[i]
        jumps[i] += 1
        i += moveTo
        steps += 1       
        
    print(f'Part One: {steps}')

def partTwo():
    
    i = 0
    steps = 0
    while i < len(jumps):
        moveTo = jumps[i]
        jumps[i] += 1
        if moveTo >= 3:
            i += 1
        else:
            i -= 1
        steps += 1    
        
    print(f'Part Two: {steps}')

partOne()
partTwo()