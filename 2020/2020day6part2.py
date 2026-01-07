import string

puzzle = open('Advent of Code Inputs/2020day6.txt').read().split('\n\n')
groups = []
res = 0

for i in puzzle:
    groups.append(i.split('\n'))

def checker(group):
    checked = {letter: 0 for letter in string.ascii_lowercase}
    size = len(group)
    ans = 0

    for person in group:
        for answer in person:
            checked[answer] += 1
    
    for i in checked:
        if checked[i] == size:
            ans += 1

    return ans


for i in groups:
    res += checker(i)

print(res)