p = open('AdventOfCode/Advent of Code Inputs/2023day4.txt').read().split('\n')
cards = []
i = 1

for card in p:
    cards.append([i, card[card.index(':') + 2:card.index('|') - 1], card[card.index('|') + 2:]])
    i += 1

puzzle = []

for i in cards:
    adder = [i[0]]
    adder.append(i[1].split())
    adder.append(i[2].split())
    puzzle.append(adder)

def partOne():

    ans = 0
    for i in puzzle:
        match = 0
        for num in i[1]:
            if num in i[2]:
                match += 1
        if match > 0:
            ans += (2 ** (match - 1))

    print(f'Part One: {ans}')

def partTwo():

    def addWinners(puzzle):
        i = 0
        while i < len(puzzle):
            match = 0
            for num in puzzle[i][1]:
                if num in puzzle[i][2]:
                    match += 1
            if match > 0:
                for j in range(match):
                    puzzle[j + i + 1][3] += puzzle[i][3]
            i += 1
        return puzzle
    
    def checkCards(puzzle):
        ans = 0
        for i in puzzle:
            ans += i[3]
        return ans
    
    for i in puzzle:
        i.append(1)
 
    res = addWinners(puzzle)
    ans = checkCards(res)
        
    print(f'Part Two: {ans}')

partOne()
partTwo()