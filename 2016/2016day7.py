import re
p = open('AdventOfCode/Advent of Code Inputs/2016day7.txt').read().split('\n')
# [[Check for abba, check for not abba, check for abba]]
puzzle = []

for line in p:
    i = re.split(r'\[|\]', line)
    puzzle.append(i)
print(puzzle)

def partOne():

    ans = 0
    
    def checkAbba(phrase, supportsIfYes=True):
        for i in range(0, len(phrase) - 3):
            if phrase[i] == phrase[i + 3] and phrase[i + 1] == phrase[i + 2] and phrase[i] != phrase[i + 1]:
                return supportsIfYes
        return not supportsIfYes

    for line in puzzle:
        for idx, phrase in enumerate(line):
            if idx % 2 == 0:
                support = True
            else:
                support = False
            if checkAbba(phrase, support) == True:
                support = False
                if checkAbba(phrase) == True or checkAbba(line[2]) == True:
                    ans += 1
                    support = True

    print(f'Part One: {ans}')

def partTwo():
    pass

partOne()
partTwo()

