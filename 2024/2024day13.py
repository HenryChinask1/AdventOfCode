import re

p = open('AdventOfCode/Advent of Code Inputs/2024day13TEST.txt').read().split('\n\n')
puzzle = []

for i in p:
    puzzle.append(re.findall(r'X\+\d+|Y\+\d+|X=\d+|Y=\d+', i))

def partOne():
    def setup(machine):
        # 3 tokens for A push.
        AX = int(machine[0][2:]) # Move right.
        AY = int(machine[1][2:]) # Move left.
        # 1 token for B push.
        BX = int(machine[2][2:])
        BY = int(machine[3][2:])
        prizeX = int(machine[4][2:])
        prizeY = int(machine[5][2:])
        return [AX, AY, BX, BY, prizeX, prizeY]
    
    def checkConfig(clawConfig):
        '''Ex 1. [94, 34, 22, 67, 8400, 5400].
            
            1) 94x + 22y = 8400 > 94x = 8400 - 22y > x = (8400 - 22y) / 94

            2) 34x + 67y = 5400 > 67y = 5400 - 34x > y = (5400 - 34x) / 67'''
        soln = 0
        for x in range(101):
            for y in range(101):
                if (x * clawConfig[0]) + (y * clawConfig[2]) == clawConfig[4] and (x * clawConfig[1]) + (y * clawConfig[3]) == clawConfig[5]:
                    soln = (x * 3) + y
        return soln  

    tokens = 0
    for i in puzzle:
        clawConfig = setup(i)
        tokens += checkConfig(clawConfig)

    print(f'Part One: {tokens}')

def partTwo():
    def setup(machine):
        # 3 tokens for A push.
        AX = int(machine[0][2:]) # Move right.
        AY = int(machine[1][2:]) # Move left.
        # 1 token for B push.
        BX = int(machine[2][2:])
        BY = int(machine[3][2:])
        prizeX = int(machine[4][2:])
        prizeY = int(machine[5][2:])
        return [AX, AY, BX, BY, prizeX, prizeY]
    
    def checkConfig(AX, AY, BX, BY, prizeX, prizeY, offset):
        soln = 0
        prize = (prizeX + offset, prizeY + offset)
        det = AX * BY - AY * BX
        a = (prize[0] * BY - prize[1] * BX) / det
        b = (AX * prize[1] - AY * prize[0]) / det
        if (AX * a + BX * b, AY * a + BY * b) == (prize[0], prize[1]):    
            soln = (a * 3) + b
        return soln

    tokens = 0
    for i in puzzle:
        clawConfig = setup(i)
        tokens += checkConfig(clawConfig[0], clawConfig[1], clawConfig[2], clawConfig[3], clawConfig[4], clawConfig[5], 10000000000000)

    print(f'Part Two: {tokens}')

partOne()
partTwo()