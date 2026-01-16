from datetime import datetime
from collections import defaultdict, Counter


def partOne():
    guardstats = []

    with open('Advent of Code Inputs/2018day4TEST.txt') as f:
        file = f.read().split('\n')
        for i in file:
            x = i.split(']')
            guardStat = []
            guardStat.append(datetime.strptime(x[0][1:], '%Y-%m-%d %H:%M'))
            guardStat.append(x[1][1:].split(' '))
            guardstats.append(guardStat)

    guardstats.sort()


    # {Guard#: minutes asleep, Guard#: minutes asleep}
    sleepTimes = defaultdict(int)
    sleptMins = defaultdict(list)
    guard = ''
    sleepStart = None
    for i in range(len(guardstats)):
        if guardstats[i][1][0] == 'Guard':
            guard = guardstats[i][1][1]
        elif guardstats[i][1][0] == 'falls':
            sleepStart = guardstats[i][0]
        elif guardstats[i][1][0] == 'wakes':
            diff = guardstats[i][0] - sleepStart
            x = diff.total_seconds()
            sleepTimes[guard] += int(x // 60)
            curr = sleepStart.minute
            while curr < guardstats[i][0].minute:
                sleptMins[guard].append(curr)
                curr += 1

    guard = max(sleepTimes, key=sleepTimes.get)
    mostMins = Counter(sleptMins[guard])
    print(f'Part One ans: {int(guard[1:]) * max(mostMins, key=mostMins.get)}')

def partTwo():

    guardstats = []

    with open('Advent of Code Inputs/2018day4TEST.txt') as f:
        file = f.read().split('\n')
        for i in file:
            x = i.split(']')
            guardStat = []
            guardStat.append(datetime.strptime(x[0][1:], '%Y-%m-%d %H:%M'))
            guardStat.append(x[1][1:].split(' '))
            guardstats.append(guardStat)

    guardstats.sort()


    # {Guard#: minutes asleep, Guard#: minutes asleep}
    sleepTimes = defaultdict(int)
    sleptMins = defaultdict(list)
    guard = ''
    sleepStart = None
    for i in range(len(guardstats)):
        if guardstats[i][1][0] == 'Guard':
            guard = guardstats[i][1][1]
        elif guardstats[i][1][0] == 'falls':
            sleepStart = guardstats[i][0]
        elif guardstats[i][1][0] == 'wakes':
            diff = guardstats[i][0] - sleepStart
            x = diff.total_seconds()
            sleepTimes[guard] += int(x // 60)
            curr = sleepStart.minute
            while curr < guardstats[i][0].minute:
                sleptMins[guard].append(curr)
                curr += 1
   
    guard = max(sleepTimes, key=sleepTimes.get)
    mostMins = Counter(sleptMins[guard])
    print(f'Part One ans: {int(guard[1:]) * max(mostMins, key=mostMins.get)}')

partOne()
partTwo()