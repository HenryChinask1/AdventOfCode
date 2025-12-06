import re

def partOne():
    data = open('Advent of Code Inputs/2025day6.txt').read().split('\n')
    mathInput = []
    for i in data[0:-1]:
        mathInput.append([int(j) for j in re.findall(r'\d+', i)])
    mathInput.append([j for j in re.findall(r'\*+|\++', data[-1])])
    # print(mathInput)
    # print(len(mathInput), len(mathInput[0]))
    ans = 0
    for i in range(1000):
        if mathInput[4][i] == '*':
            ans += (mathInput[0][i] * mathInput[1][i] * mathInput[2][i] * mathInput[3][i])
        else:
            ans += sum([mathInput[0][i], mathInput[1][i], mathInput[2][i], mathInput[3][i]])
    print(f'Part One: {ans}')

def partTwo():
    pass

partOne()
partTwo()