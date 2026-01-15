import re
p = open('Advent of Code Inputs/2016day7.txt').read().split('\n')
# [[Check for abba, check for not abba, check for abba]]
puzzle = []

for line in p:
    start = 0
    puzLine = []
    for i in range(len(line)):
        if line[i] == '[':
            puzLine.append(['in', line[start:i]])
            start = i + 1
        elif line[i] == ']':
            puzLine.append(['out', line[start:i]])
            start = i + 1
        elif i == len(line) - 1:
            puzLine.append(['in', line[start:]])
            start = 0
            puzzle.append(puzLine)
            puzLine = []

def partOne():

    ans = 0
    
    def checkAbba(phrase):
        for i in range(0, len(phrase) - 3):
            if phrase[i] == phrase[i + 3] and phrase[i + 1] == phrase[i + 2] and phrase[i] != phrase[i + 1]:
                return True
        return False

    for line in puzzle:
        supports = False
        for piece in line:
            if piece[0] == 'in':
                supports = max(supports, checkAbba(piece[1]))
            elif piece[0] == 'out' and checkAbba(piece[1]):
                supports = False
                break
        if supports:
            ans += 1
            supports = False

    print(f'Part One: {ans}')

def partTwo():
    pass

partOne()
partTwo()