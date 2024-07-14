import string

alphaCount = dict.fromkeys(string.ascii_lowercase, 0)
twos = 0
threes = 0


boxes = open('boxScans.txt').read().split('\n')

for idx, letter in enumerate(boxes):
    if letter in alphaCount:
        alphaCount[letter] += 1
    options = alphaCount.values()
    for i in options:
        if i == 2:
            twos += 1
        if i == 3:
            threes += 1
    