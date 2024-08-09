import string

twos = 0
threes = 0
commonBoxes = []


boxes = open('Advent of Code Inputs/2018day2.txt').read().split()
#print(boxes)

for box in boxes:
    alphaCount = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in box:
        alphaCount[letter] += 1
    #print(alphaCount)

    if 2 in alphaCount.values():
        twos += 1
        commonBoxes.append(box)
    if 3 in alphaCount.values():
        threes += 1
        commonBoxes.append(box)

print('Part One:')
print(twos * threes)

def diffLetters(a, b):
    twoWords = zip(a, b)
    checker = [0, '', '']
    for item in twoWords:
        if item[0] != item[1]:
            checker[0] += 1
            checker[1] += '*'
            checker[2] += '*'
        else:
            checker[1] += item[0]
            checker[2] += item[1]
    
    return checker

for a in commonBoxes:
    for b in commonBoxes:
        if 1 in diffLetters(a, b):
            print('Part Two:')
            print(diffLetters(a, b)[2])