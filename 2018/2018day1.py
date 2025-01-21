p = open('AdventOfCode/Advent of Code Inputs/2018day1.txt').read().split('\n')

def partOne():
    freq = 0
    for i in p:
        if i[0] == '+':
            freq += int(i[1:])
        elif i[0] == '-':
            freq -= int(i[1:])
    print(f'Part One: {freq}')

def partTwo():
    frequencies = {0: 1}
    freq = 0
    i = 0
    while True:
        if p[i][0] == '+':
            freq += int(p[i][1:])
        elif p[i][0] == '-':
            freq -= int(p[i][1:])
        if freq in frequencies:
            print(f'Part Two: {freq}')
            break
        else:
            frequencies[freq] = 1
        if i == len(p) - 1:
            i = 0
        else:
            i += 1
partOne()
partTwo()