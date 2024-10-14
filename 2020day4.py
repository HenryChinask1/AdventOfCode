passports = open('Advent of Code Inputs/2020day4TEST.txt').read().split('\n\n')

valids = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for i in passports:
    for j in valids:
        if j in i:
            