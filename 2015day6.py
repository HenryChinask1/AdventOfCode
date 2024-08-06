lightGrid = [[0 for i in range(1000)] for i in range(1000)] #One million light grid with 1000x1000 rows.

moves = open('2015day6.txt').read().split('\n')
movesList = []

for i in moves:
    if i.startswith('turn on'):
        move = i.split(' ')
        movesList.append(['on', move[2], move[4]])
    elif i.startswith('toggle'):
        move = i.split(' ')
        movesList.append(['toggle', move[1], move[3]])
    elif i.startswith('turn off'):
        move = i.split(' ')
        movesList.append(['off', move[2], move[4]])

def coordParse(move):
    x1, y1 = i[1].split(',')
    x2, y2 = i[2].split(',')


for i in movesList:
    if i[0] == 'on':
        x1, y1 = i[1].split(',')
        x2, y2 = i[2].split(',')
        for row in range(int(x1), int(x2) + 1):
            for col in range(int(y1), int(y2) + 1):
                lightGrid[row][col] = 1
    elif i[0] == 'toggle':
        x1, y1 = i[1].split(',')
        x2, y2 = i[2].split(',')
        for row in range(int(x1), int(x2) + 1):
            for col in range(int(y1), int(y2) + 1):
                if lightGrid[row][col] == 0:
                    lightGrid[row][col] = 1
                else:
                    lightGrid[row][col] = 0
    elif i[0] == 'off':
        x1, y1 = i[1].split(',')
        x2, y2 = i[2].split(',')
        for row in range(int(x1), int(x2) + 1):
            for col in range(int(y1), int(y2) + 1):
                lightGrid[row][col] = 0

ans = 0

for i in lightGrid:
    for j in i:
        if j == 1:
            ans += 1

print(ans)