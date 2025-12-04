def partOne():
    data = open('Advent of Code Inputs/2025day4.txt').read().split('\n')
    racks = ['.' * (len(data[0]) + 2)]
    for i in data:
        racks.append('.' + i + '.')
    racks.append('.' * len(racks[0]))
    ans = 0  

    def checkAdj(racks, x, y):
        rollsTouching = 0
        dirs = [(0, 1), (0, -1), (1, 1), (-1, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]

        for coord in dirs:
            if racks[x + coord[0]][y + coord[1]] == '@':
                rollsTouching += 1
        
        if rollsTouching < 4:
            return 1
        return 0
    
    
    for i in range(len(racks)):
        for j in range(len(racks[0])):
            if racks[i][j] == '@':
                ans += checkAdj(racks, i, j)
    print(f'Part One: {ans}')

def partTwo():
    data = open('Advent of Code Inputs/2025day4.txt').read().split('\n')
    racks = [['.'] * (len(data[0]) + 2)]
    for i in data:
        racks.append(list('.' + i + '.'))
    racks.append(['.'] * len(racks[0]))
    ans = 0  

    def checkAdj(racks, x, y):
        rollsTouching = 0
        dirs = [(0, 1), (0, -1), (1, 1), (-1, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]

        for coord in dirs:
            if racks[x + coord[0]][y + coord[1]] == '@' or racks[x + coord[0]][y + coord[1]] == 'X':
                rollsTouching += 1
        
        if rollsTouching < 4:
            racks[x][y] = 'X'
            return 1
        return 0
    
    def updateList(racks):
        for i in range(len(racks)):
            for j in range(len(racks[0])):
                if racks[i][j] == 'X':
                    racks[i][j] = '.'
        return racks
    
    tempAns = 1
    while ans != tempAns:
        tempAns = ans
        for i in range(len(racks)):
            for j in range(len(racks[0])):
                if racks[i][j] == '@':
                    ans += checkAdj(racks, i, j)
                    racks = updateList(racks)
    print(f'Part Two: {ans}')

partOne()
partTwo()