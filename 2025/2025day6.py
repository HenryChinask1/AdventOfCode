import re

def partOne():
    data = open('Advent of Code Inputs/2025day6.txt').read().split('\n')
    mathInput = []
    for i in data[0:-1]:
        mathInput.append([int(j) for j in re.findall(r'\d+', i)])
    mathInput.append([j for j in re.findall(r'\*+|\++', data[-1])])
    ans = 0
    for i in range(1000):
        if mathInput[4][i] == '*':
            ans += (mathInput[0][i] * mathInput[1][i] * mathInput[2][i] * mathInput[3][i])
        else:
            ans += sum([mathInput[0][i], mathInput[1][i], mathInput[2][i], mathInput[3][i]])
    print(f'Part One: {ans}')

def partTwo():

    data = open('Advent of Code Inputs/2025day6.txt').read().split('\n')
    mathInput = []
    ans = []
    newSigns = []

    for i in data[-1]:
        if i in '+*':
            newSigns.append(i)
        else:
            newSigns.append(newSigns[-1])
    mathInput.append(newSigns)

    for i in data[:-1]:
        mathInput.append([j if j != ' ' else '' for j in i])

    tempAns = 0
    sign = mathInput[0][-1]
    for x in range(len(mathInput[0]) - 1, -1, -1):
        if sign == '+':
            num = mathInput[1][x] + mathInput[2][x] + mathInput[3][x] + mathInput[4][x]
            if num == '':
                ans.append(tempAns)
                sign = mathInput[0][x - 1]
                tempAns = 1 if sign == '*' else 0
            else:
                tempAns += int(num)
        elif sign == '*':
            num = mathInput[1][x] + mathInput[2][x] + mathInput[3][x] + mathInput[4][x]
            if num == '':
                ans.append(tempAns)
                sign = mathInput[0][x - 1]
                tempAns = 1 if sign == '*' else 0
            else:
                tempAns *= int(num)
    ans.append(tempAns)

    print(f'Part Two: {sum(ans)}')

partOne()
partTwo()