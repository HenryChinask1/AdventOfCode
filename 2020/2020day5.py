p = open("Advent of Code Inputs/2020day5.txt").read().split()
seatId = []


def rowCalc(boarder):
    row = (0, 127)
    col = (0, 7)
    finalRow = 0
    finalCol = 0

    for i in range(6):
        if boarder[i] == 'F':
            row = (row[0], ((row[1] - row[0]) // 2) + row[0])
            #print(row)
        if boarder[i] == 'B':
            row = (row[0] + ((row[1] - row[0]) // 2) + 1, row[1])
            #print(row)
    finalRow = row[0] if boarder[6] == 'F' else row[1]
    #print(finalRow)

    for i in range(7, 9):
        if boarder[i] == 'L':
            col = (col[0], ((col[1] - col[0]) // 2) + col[0])
            #print(col)
        if boarder[i] == 'R':
            col = (col[0] + ((col[1] - col[0]) // 2) + 1, col[1])
            #print(col)
    finalCol = col[0] if boarder[9] == 'L' else col[1]
    #print(finalCol)
    newId = finalRow * 8 + finalCol
    return newId

for boarder in p:
    seatId.append(rowCalc(boarder))

#print(seatId)
print(max(seatId))