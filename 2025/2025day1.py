def partOne():
    data = open('Advent of Code Inputs/2025day1.txt').read().split('\n')
    turns = [(i[0], int(i[1:])) for i in data]
    res = 0

    currDial = 50

    def countUp(currDial, turn):
        while turn:
            currDial += 1
            turn -= 1
            if currDial > 99:
                currDial = 0
        return currDial
    
    def countDown(currDial, turn):
        while turn:
            currDial -= 1
            turn -= 1
            if currDial < 0:
                currDial = 99
        return currDial

    for turn in turns:
        if currDial == 0:
            res += 1
        if turn[0] == 'L':
            currDial = countDown(currDial, turn[1])
        else:
            currDial = countUp(currDial, turn[1])
    print(res)

def partTwo():

    data = open('Advent of Code Inputs/2025day1.txt').read().split('\n')
    turns = [(i[0], int(i[1:])) for i in data]
    currDial = [0, 50]

    def countUp(currDial, turn, res):
        while turn:
            currDial += 1
            turn -= 1
            if currDial == 0:
                res += 1
            if currDial > 99:
                currDial = 0
                res += 1
        return [res, currDial]
    
    def countDown(currDial, turn, res):
        while turn:
            currDial -= 1
            turn -= 1
            if currDial == 0:
                res += 1
            if currDial < 0:
                currDial = 99
        return [res, currDial]

    for turn in turns:
        if turn[0] == 'L':
            currDial = countDown(currDial[1], turn[1], currDial[0])
        else:
            currDial = countUp(currDial[1], turn[1], currDial[0])
        
    print(currDial[0])

partOne()
partTwo()