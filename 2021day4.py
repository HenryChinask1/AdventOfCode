# Set up input.
bingoCards = open('Advent of Code Inputs/2021day4b.txt').read().split()
bingoDraws = open('Advent of Code Inputs/2021day4a.txt').read().split(',')
cardMap = []
firstWinner = 0
lastWinner = 0

# Create the map.
for i in range(0, len(bingoCards), 25):
    cardMap.append(bingoCards[i:i + 25])

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
            ans = 0
            for i in b:
                if i != 'X':
                    ans += int(i)
            return ans

# Update the list in-place (I think).
def listReplace(lst, old, new):
    for idx, value in enumerate(lst):
        if isinstance(value, list):
            listReplace(value, old, new)
        else:
            if value == old:
                lst[idx] = new
    return lst


# Main loop. Iterate draws and check for a winner after each draw.
def getFirstWinner():    
    for i in bingoDraws:
        for idx, value in enumerate(cardMap):
            #print(idx, value, i)
            if str(i) in value:
                listReplace(value, str(i), 'X')
            #print(idx, value, i)
                if isWinner(cardMap):
                    firstWinner = isWinner(cardMap)
                    return firstWinner * int(i)

print(f'Answer Part 1: {getFirstWinner()}')
