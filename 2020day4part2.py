p = open('Advent of Code Inputs/2020day4.txt').read().split('\n\n')
passports = []
for line in p:
    passports.append(line.split())

ans = 0

def checkValid(passport):
    passportDict = {}
    for i in passport:
        key, value = i.split(':', 1)
        passportDict[key] = value

    valids = {'byr': [1920, 2002], 'iyr': [2010, 2020], 'eyr': [2020, 2030], 
              'hgt': ['cm', 150, 193, 'in', 59, 76], 'hcl': ['#', 6, '1234567890abcdef'], 
              'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 'pid': [9, '0123456789']}
    for key in valids:
        if key not in passportDict:
            return 0
    
    for key in passportDict:
        if key not in valids and key != 'cid':
            return 0
        if key == 'byr':
            try:
                if int(passportDict[key]) > valids[key][1] or int(passportDict[key]) < valids[key][0]:
                    return 0
            except:
                return 0
        if key == 'iyr':
            try:
                if int(passportDict[key]) > valids[key][1] or int(passportDict[key]) < valids[key][0]:
                    return 0
            except:
                return 0
        if key == 'eyr':
            try:
                if int(passportDict[key]) > valids[key][1] or int(passportDict[key]) < valids[key][0]:
                    return 0
            except:
                return 0
        if key == 'hgt':
            if 'cm' in passportDict[key]:
                try:
                    if int(passportDict[key][0:3]) > valids[key][2] or int(passportDict[key][0:3]) < valids[key][1]:
                        return 0
                except:
                    return 0
            elif 'in' in passportDict[key]:
                try:
                     if int(passportDict[key][0:2]) > valids[key][5] or int(passportDict[key][0:2]) < valids[key][4]:
                         return 0
                except:
                    return 0
            else:
                return 0
        if key == 'hcl':
            if passportDict[key][0] != '#':
                return 0
            if len(passportDict[key]) != 7:
                return 0
            for i in passportDict[key][1:]:
                if i not in '0123456789abcdef':
                    return 0
        if key == 'ecl':
            if passportDict[key] not in valids['ecl']:
                return 0
        if key == 'pid':
            if len(passportDict[key]) != 9:
                return 0
            for i in passportDict[key]:
                if i not in '0123456789':
                    return 0
    return 1

for passport in passports:
    ans += checkValid(passport)      

print(ans)