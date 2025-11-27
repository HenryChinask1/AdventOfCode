import itertools
p = open('Advent of Code Inputs/2024day7.txt').read().split('\n')
puzzle = {}
for i in p:
    puzzle[int(i[0:i.index(':')])] = i[i.index(':') + 2:]
for i in puzzle:
    puzzle[i] = puzzle[i].split(' ')
for i in puzzle:
    puzzle[i] = [i for i in puzzle[i]]


def partOne():
    opers = '+*'
    ans = 0

    def calc(eq):
        res = 0
        oper = '+'
        num = ''

        for char in eq:
            if char.isdigit():
                num += char
            else:
                if num:
                    if oper == '+':
                        res += int(num)
                    elif oper == '*':
                        res *= int(num)
                num = ''
                oper = char
        if num:
            if oper == '+':
                res += int(num)
            elif oper == '*':
                res *= int(num)
        return res

    for total, equation in puzzle.items():
        combos = list(itertools.product(opers, repeat=len(equation) - 1))
        for combo in combos:
            eq = []
            for i in range(len(equation) - 1):
                eq.append(equation[i])
                eq.append(combo[i])
            eq.append(equation[-1])
            if calc(''.join(i for i in eq)) == total:
                ans += total
                break
    print(f'Part One: {ans}')
            
def partTwo():
    opers = '+*_'
    ans = 0

    def calc(eq):
        res = 0
        oper = '+'
        num = ''

        for char in eq:
            if char.isdigit():
                num += char
            else:
                if num:
                    if oper == '+':
                        res += int(num)
                    elif oper == '*':
                        res *= int(num)
                    elif oper == '_':
                        res = int(str(res) + num)
                num = ''
                oper = char
        if num:
            if oper == '+':
                res += int(num)
            elif oper == '*':
                res *= int(num)
            elif oper == '_':
                res = int(str(res) + num)
        return res

    for total, equation in puzzle.items():
        combos = list(itertools.product(opers, repeat=len(equation) - 1))
        for combo in combos:
            eq = []
            for i in range(len(equation) - 1):
                eq.append(equation[i])
                eq.append(combo[i])
            eq.append(equation[-1])
            if calc(''.join(i for i in eq)) == total:
                ans += total
                break
    print(f'Part Two: {ans}')

partOne()
partTwo()