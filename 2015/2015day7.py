import numpy as np
from collections import defaultdict

input = open('Advent of Code Inputs/2015day7TEST.txt').read().split('\n')

circuits = []

for i in input:
    circuits.append(i.split(' '))

def Sort(circuits):
    l = len(circuits)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (circuits[j][-1] > circuits[j + 1][-1]):
                tempo = circuits[j]
                circuits[j] = circuits[j + 1]
                circuits[j + 1] = tempo
    
    return circuits

# puzzleInput = circuits
puzzleInput = Sort(circuits)
circuits.sort(key=len)

ans = defaultdict()

def checkVals(parts, op):
    if op == 'NOT':
        return ['NOT', parts[1], parts[2]] # Both are letters.
    
    elif op == 'ASSIGN':
        part1 = np.uint16(parts[0])
        part2 = parts[2]
        return [part1, part2]

    else:
        if parts[0].isdigit():
            part1 = np.uint16(int(parts[0]))
        else:
            part1 = parts[0]
        if parts[2].isdigit():
            part2 = np.uint16(int(parts[2]))
        else:
            part2 = parts[1]
        if parts[4].isdigit():
            part3 = np.uint16(int(parts[4]))
        else:
            part3 = parts[4]
        return [op, part1, part2, part3]


for i in range(len(puzzleInput)):
    if 'NOT' in puzzleInput[i]:
        parts = checkVals(puzzleInput[i], 'NOT')
        ans[parts[0]] = ~ans[parts[1]]
    elif 'AND' in puzzleInput[i]:
        parts = checkVals(puzzleInput[i], 'AND')
        ans[parts[4]] = ans[parts[2]] & ans[parts[3]]
    elif 'OR' in puzzleInput[i]:
        parts = checkVals(puzzleInput[i], 'OR')
        ans[parts[4]] = ans[parts[2]] | ans[parts[3]]
    elif 'LSHIFT' in puzzleInput[i]:
        parts = checkVals(puzzleInput[i], 'LSHIFT')
        ans[parts[4]] = ans[parts[2]] << ans[parts[3]]
    elif 'RSHIFT' in puzzleInput[i]:
        parts = checkVals(puzzleInput[i], 'RSHIFT')
        ans[parts[4]] = ans[parts[2]] >> ans[parts[3]]
    else:
        parts = checkVals(puzzleInput[i], 'ASSIGN')
        ans[parts[1]] = parts[0]

print(ans)
print(f'Part One: {ans['a']}')