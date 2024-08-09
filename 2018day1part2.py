from collections import Counter

freqChanges = open('Advent of Code Inputs/2018day1.txt')


def loopFreq(freqChanges):
    ans = 0
    freqEnds = []
    for i in freqChanges:
        if i == ' ':
            continue
        if i[0] == '+':
            ans += int(i[1:])
            freqEnds.append(int(ans))
            if ans in freqEnds:
                print(ans)
        if i[0] == '-':
            ans -= int(i[1:])
            freqEnds.append(int(ans))
            if ans in freqEnds:
                print(ans)
    print(ans)
    return freqEnds


freqEnds = loopFreq(freqChanges)
firstDoop = []

for i in freqEnds:
    firstDoop = []
    if freqEnds.count(i) > 1:
        if i != 0:
            firstDoop.append(i)

while not firstDoop:
    loopFreq(freqChanges)
    



