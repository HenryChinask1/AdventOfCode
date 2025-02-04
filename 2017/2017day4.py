f = open('AdventOfCode/Advent of Code Inputs/2017day4.txt').read().split('\n')

def partOne():
    ans = 0

    for line in f:
        words = line.split(' ')
        phrases = []
        for word in words:
            phrases.append(word)
        if len(phrases) == len(set(phrases)):
            ans += 1
    print(f'Part One: {ans}')

def partTwo():
    ans = 0

    for line in f:
        words = line.split(' ')
        phrases = []
        for word in words:
            phrases.append(''.join(sorted(word)))
        if len(phrases) == len(set(phrases)):
            ans += 1
    print(f'Part Two: {ans}')

partOne()
partTwo()