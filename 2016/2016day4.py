from collections import Counter
p = open('AdventOfCode/Advent of Code Inputs/2016day4.txt').read().split('\n')
# A list of tuples ['room name', 'sectorID', 'checksum']
puzzle = []

for i in p:
    for char in i:
        if char.isdigit():
            puzzle.append([i[0:i.index(char)], i[i.index(char):i.index('[')], i[i.index('['):]])
            break


def partOne():

    rooms = 0
    
    def checkRoom(name):
        checkCount = {(ord(i) - ord('a')):0 for i in name if i not in '-'}
        for i in name:
            if (ord(i) - ord('a')) in checkCount:
                checkCount[(ord(i) - ord('a'))] += 1
        return checkCount
    
    def validRoom(checkCount, sectorID, rooms, checkSum):
        checkSum = [(ord(i) - ord('a')) for i in checkSum if i not in '[]']
        # Check count is letter(int): count(int).
        if checkSum[0] not in checkCount:
            return rooms
        currTotal = checkCount[checkSum[0]]
        ID = int(sectorID)
        for i in range(1, len(checkSum)):
            if checkSum[i] not in checkCount:
                return rooms
            elif checkCount[checkSum[i]] > currTotal:
                return rooms
            elif checkCount[checkSum[i]] == currTotal:
                if checkSum[i - 1] > checkSum[i]:
                    return rooms
            currTotal = checkCount[checkSum[i]]
        rooms += ID
        return rooms


    for i in puzzle:
        checkCount = checkRoom(i[0])
        rooms = validRoom(checkCount, i[1], rooms, i[2])
    print(f'Part One: {rooms}') 

def partTwo():
    pass

partOne()
partTwo()