# Set up input.
bingoCards = open('bingoCards.txt').read().split()
bingoDraws = open('bingoDraws.txt').read().split(',')
cardMap = []
firstWinner = 0
lastWinner = 0

# Create the map.
for i in range(0, len(bingoCards), 25):
    cardMap.append(bingoCards[i:i + 25])

# Check if any card has won after a draw.
def isLastWinner(board):
    for b in board:
        if (((b[0] == b[1] == b[2] == b[3] == b[4] == 'X') or # ROW 1 clear.
        (b[5] == b[6] == b[7] == b[8] == b[9] == 'X') or # ROW 2 clear.
        (b[10] == b[11] == b[12] == b[13] == b[14] == 'X') or # ROW 3 clear.
        (b[15] == b[16] == b[17] == b[18] == b[19] == 'X') or # ROW 4 clear.
        (b[20] == b[21] == b[22] == b[23] == b[24] == 'X') or # ROW 5 clear.
        (b[0] == b[5] == b[10] == b[15] == b[20] == 'X') or # COLUMN 1 clear.
        (b[1] == b[6] == b[11] == b[16] == b[21] == 'X') or # COLUMN 2 clear.
        (b[2] == b[7] == b[12] == b[17] == b[22] == 'X') or # COLUMN 3 clear.
        (b[3] == b[8] == b[13] == b[18] == b[23] == 'X') or # COLUMN 4 clear.
        (b[4] == b[9] == b[14] == b[19] == b[24] == 'X')) and len(board) > 1): # COLUMN 5 clear.
            board.remove(b)
    return board

# Final card checker.
def isWinner(board):
    for b in board:
        if ((b[0] == b[1] == b[2] == b[3] == b[4] == 'X') or # ROW 1 clear.
        (b[5] == b[6] == b[7] == b[8] == b[9] == 'X') or # ROW 2 clear.
        (b[10] == b[11] == b[12] == b[13] == b[14] == 'X') or # ROW 3 clear.
        (b[15] == b[16] == b[17] == b[18] == b[19] == 'X') or # ROW 4 clear.
        (b[20] == b[21] == b[22] == b[23] == b[24] == 'X') or # ROW 5 clear.
        (b[0] == b[5] == b[10] == b[15] == b[20] == 'X') or # COLUMN 1 clear.
        (b[1] == b[6] == b[11] == b[16] == b[21] == 'X') or # COLUMN 2 clear.
        (b[2] == b[7] == b[12] == b[17] == b[22] == 'X') or # COLUMN 3 clear.
        (b[3] == b[8] == b[13] == b[18] == b[23] == 'X') or # COLUMN 4 clear.
        (b[4] == b[9] == b[14] == b[19] == b[24] == 'X')): # COLUMN 5 clear.
            return True
    return board


# Update the list in-place (I think).
def listReplace(lst, old, new):
    for idx, value in enumerate(lst):
        if isinstance(value, list):
            listReplace(value, old, new)
        else:
            if value == old:
                lst[idx] = new
    return lst

# Iterate through the cards for each draw and check for a winner after each replacement.        
def getLastWinner(cardMap):
    for i in bingoDraws:
        for idx, value in enumerate(cardMap):
            if str(i) in value:
                listReplace(value, str(i), 'X')
                lastWinner = isLastWinner(cardMap)
                #print(lastWinner, i)
                #print(lastWinner)
                if len(lastWinner) == 1:
                    listReplace(lastWinner, str(i), 'X')
                    #print(lastWinner, i)
                    if isWinner(lastWinner) == True:
                        return calcAnswer(lastWinner, i)




# Multiply the sum of the values left on the card by the last drawn number.
def calcAnswer(finalCard, finalDraw):
    ans = 0
    for i in finalCard[0]:
        if i != 'X':
            ans += int(i)
    print(ans, finalDraw)
    return int(ans) * int(finalDraw)


print(f'Answer Part 2: {getLastWinner(cardMap)}')