import re

calDoc = open('Advent of Code Inputs/2023day1.txt').read().split('\n')

def getDigit(x):
    return x if x.isnumeric() else str(letterDigits.index(x))

letterDigits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))'
total = 0

for line in calDoc:
    digits = re.findall(regex, line)
    total += int(getDigit(digits[0]) + getDigit(digits[-1]))


print(f'Part Two: {total}')