passports = open('Advent of Code Inputs/2020day4.txt').read().split('\n\n')

ans = 0

def checkValid(passport):
    valids = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for valid in valids:
        if valid not in passport:
            return 0
    return 1

for passport in passports:
    ans += checkValid(passport)      

print(ans)