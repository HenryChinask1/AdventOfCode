from collections import Counter

freqChanges = open('calibration.txt')

ans = 0
freqEnds = []
ans2 = 574
ans3 = 1148
ans4 = 1722
ans5 = 2296

for i in freqChanges:
        if i == ' ':
            continue
        if i[0] == '+':
            ans += int(i[1:])
            freqEnds.append(int(ans))
        if i[0] == '-':
            ans -= int(i[1:])
            freqEnds.append(int(ans))

for i in freqEnds:
    while i no



set([i for i in freqEnds if freqEnds.count(i) > 1])
print(freqEnds)


print(ans)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
