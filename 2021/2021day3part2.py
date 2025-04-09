power = open("AdventOfCode/Advent of Code Inputs/2021day3.txt").read().split('\n')
width = len(power[0])

bitMax = power[:]
o2Gen = 0
co2Scrub = 0

def checkMax(bits:list, pos:int) -> list:
    # Check for the max bits in the curr pos and return a list of values that comply.
    ones = 0
    zeros = 0
    goodBits = []
    for i in bits:
        if i[pos] == '1':
            ones += 1
        elif i[pos] == '0':
            zeros += 1
    bit = '1' if max(ones, zeros) == ones else '0'

    for i in bits:
        if i[pos] == bit:
            goodBits.append(i)
    return goodBits

def checkMin(bits:list, pos:int) -> list:
    # Check for the min bits in the curr pos and return a list of values that comply.
    ones = 0
    zeros = 0
    goodBits = []
    for i in bits:
        if i[pos] == '1':
            ones += 1
        elif i[pos] == '0':
            zeros += 1
    bit = '0' if min(ones, zeros) == zeros else '1'

    for i in bits:
        if i[pos] == bit:
            goodBits.append(i)
    return goodBits

for i in range(width):
    bitMax = checkMax(bitMax, i)
    if len(bitMax) == 1:
        break
o2Gen = int(bitMax[0], 2)

bitMax = power[:]

for i in range(width):
    bitMax = checkMin(bitMax, i)
    if len(bitMax) == 1:
        break
co2Scrub = int(bitMax[0], 2)

print(f'Part Two: {o2Gen * co2Scrub}')