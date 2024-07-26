import string

twos = 0
threes = 0
commonBoxes = []


boxes = open('2018day2.txt').read().split()
#print(boxes)

for box in boxes:
    alphaCount = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in box:
        alphaCount[letter] += 1
    print(alphaCount)

    if 2 in alphaCount.values():
        twos += 1
        commonBoxes.append(box)
    if 3 in alphaCount.values():
        threes += 1
        commonBoxes.append(box)

print(twos * threes)
print(commonBoxes)