from collections import Counter

freqChanges = open('Advent of Code Inputs/2018day1.txt')

start = 0
freqEnds = []

def changeLog(freqChanges, start, freqHits):
    hits = start
    freqEnds = freqHits
    for i in freqChanges:
            if i[0] == '+':
                hits += int(i[1:])
                freqEnds.append(int(hits))
                if freqEnds.count(int(hits)) > 1:
                     return hits
            if i[0] == '-':
                hits -= int(i[1:])
                freqEnds.append(int(hits))
                if freqEnds.count(int(hits)) > 1:
                     return hits
    changeLog(freqChanges, freqEnds[-1], freqEnds)


# def checkForHits(freqEnds, ans):
#     for i in freqEnds:
#         if freqEnds.count(i) > 1:
#             return i
#     changeLog(freqChanges, start)
#     checkForHits(freqEnds, ans)

ans = changeLog(freqChanges, start, freqEnds)


print(ans)