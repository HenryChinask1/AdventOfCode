# [['rect', 'AxB'] OR ['rotate', (column or row), (x=A or y=A), 'by', B]]
moves = []
screen = [['.'] * 50 for _ in range(6)]

with open("Advent of Code Inputs/2016day8.txt", "r") as f:
    file = f.read().split('\n')
    for i in file:
        if i[1] == 'e':
            x = i.split(' ')
            vals = x[1].split('x')
            move = ['rect', int(vals[0]), int(vals[1])]
            moves.append(move)
        else:
            x = i.split(' ')
            val1 = x[2].split('=')
            move = ['rotate', val1[0], int(val1[1]), int(x[-1])]
            moves.append(move)

def updateRect(screen, change):
    for i in range(change[2]):
        for j in range(change[1]):
            screen[i][j] = "#"
    return screen

def rotateColX(screen, change):
    origCol = []
    col = change[2]
    rotate = -change[3]
    for i in range(len(screen)):
        origCol.append(screen[i][col])
    newCol = origCol[rotate:] + origCol[:rotate]
    for i in range(len(screen)):
        screen[i][col] = newCol[i]
    return screen

def rotateColY(screen, change):
    origRow = []
    row = change[2]
    rotate = -change[3]
    for i in range(len(screen[0])):
        origRow.append(screen[row][i])
    newRow = origRow[rotate:] + origRow[:rotate]
    for i in range(len(screen[0])):
        screen[row][i] = newRow[i]
    return screen

for i in moves:
    if i[0] == 'rect':
        updateRect(screen, i)
    elif i[1] == 'x':
        rotateColX(screen, i)
    elif i[1] == 'y':
        rotateColY(screen, i)

ans = 0
for i in range(len(screen)):
    for j in range(len(screen[0])):
        if screen[i][j] == "#":
            ans += 1
print(f'Part One ans: {ans}')
print(f'Part Two ans:')
for i in screen:
    print(f'{''.join(i)}')