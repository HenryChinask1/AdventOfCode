crateStack = [['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
              ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
              ['C', 'V', 'S', 'H'],
              ['H', 'F', 'G'],
              ['P', 'G', 'J', 'B', 'Z'],
              ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
              ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
              ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
              ['W', 'P' ,'V', 'M', 'B', 'H']]


crateMoves = open('crateMoves.txt').read().split('\n')

# numToMove = moveList[1], stackFrom = moveList[3], stackTo = moveList[5]
moveList = [i.split(' ') for i in crateMoves]



for move in moveList:
    for i in range(int(move[1])):
        mover = crateStack[int(move[3]) - 1].pop()
        crateStack[int(move[5]) - 1].append(mover)

for i in crateStack:
    print(i[-1])
