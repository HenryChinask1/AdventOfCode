from collections import Counter
p = open('Advent of Code Inputs/2016day4.txt').read().split('\n')
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

    rooms = []
    
    def checkRoom(name):
        checkCount = {(ord(i) - ord('a')):0 for i in name if i not in '-'}
        for i in name:
            if (ord(i) - ord('a')) in checkCount:
                checkCount[(ord(i) - ord('a'))] += 1
        return checkCount
    
    def validRoom(checkCount, sectorID, checkSum):
        checkSum = [(ord(i) - ord('a')) for i in checkSum if i not in '[]']
        # Check count is letter(int): count(int).
        if checkSum[0] not in checkCount:
            return
        currTotal = checkCount[checkSum[0]]
        ID = int(sectorID)
        for i in range(1, len(checkSum)):
            if checkSum[i] not in checkCount:
                return
            elif checkCount[checkSum[i]] > currTotal:
                return
            elif checkCount[checkSum[i]] == currTotal:
                if checkSum[i - 1] > checkSum[i]:
                    return
            currTotal = checkCount[checkSum[i]]
        
        return sectorID
    
    def decrypt(phrase, rotation):
        newPhrase = []
        for i in phrase:
            if i == '-':
                newPhrase.append(' ')
            else:
                newPhrase.append(chr(((ord(i) - ord('a') + rotation) % 26) + 97))
        return ''.join(i for i in newPhrase)

    for i in puzzle:
        checkCount = checkRoom(i[0])
        rooms.append(validRoom(checkCount, i[1], i[2]))

    for i in puzzle:
        if i[1] in rooms:
            room = decrypt(i[0], int(i[1]))
            print(room)
            if 'object' in room:
                print(f'Part Two: {i[1]}')
                break

partOne()
partTwo()