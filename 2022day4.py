cleanLoc = open('sectionIDs.txt').read().replace('-',',').split('\n')

elfLoc = [i.split(',') for i in cleanLoc]
ans = 0
ans2 = 0

#print(elfLoc)

# Part 1.
for idx, group in enumerate(elfLoc):
    if int(group[0]) >= int(group[2]) and int(group[1]) <= int(group[3]):
        ans += 1
    elif int(group[2]) >= int(group[0]) and int(group[3]) <= int(group[1]):
        ans += 1

# Part 2.
for idx, group in enumerate(elfLoc):
    if int(group[0]) <= int(group[3]) and int(group[1]) >= int(group[2]):
        ans2 += 1
    elif int(group[2]) <= int(group[1]) and int(group[3]) >= int(group[0]):
        ans2 += 1

print(f'Part 1: {ans}')
print(f'Part 2: {ans2}')