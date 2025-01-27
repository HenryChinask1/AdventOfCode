import re

p = open('AdventOfCode/Advent of Code Inputs/2018day4TEST.txt').read().split('\n')

guardTimes = []
guardNum = 0
for i in p:
    date = re.findall(r'\d{4}-\d{2}-\d{2}', i)
    time = re.findall(r'\d{2}:\d{2}', i)
    if re.findall(r'#\d+', i):
        guardNum = re.findall(r'#(\d+)', i)
    state = re.findall(r'begins|asleep|wakes', i)
    guardTimes.append([guardNum[0], date[0], time[0], state[0]])

def partOne():
    allGuards = []
    for i in guardTimes:
        allGuards.append(i[0])
    
    guardStats = {i: [(j, 0) for j in range(0, 76)] for i in set(allGuards)}
    print(guardStats)

    for i in guardTimes:
        if guardStats[i]:
            guardStats[i[0]][guardStats] = 1

def partTwo():
    pass

partOne()
partTwo()