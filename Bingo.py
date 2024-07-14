import random

#Constants.
B = [str(i) for i in range(1, 16)]
I = [str(i) for i in range(16, 31)]
N = [str(i) for i in range(30, 46)]
G = [str(i) for i in range(45, 61)]
O = [str(i) for i in range(60, 76)]
FREE = 'X'
drawPool = list(i for i in range(1, 76))

# Create Bingo cards.
def getBingoCards():
    board = []
    random.shuffle(B)
    random.shuffle(I)
    random.shuffle(N)
    random.shuffle(G)
    random.shuffle(O)

    for i in range(5):
        board.append([B[i],
                      I[i],
                      N[i],
                      G[i],
                      O[i]])
    board[2][2] = FREE
    return board

cards = [getBingoCards() for i in range(101)] #100 Random Bingo Cards created.

def getBoardStr(card):
    # Return a text representation of BINGO cards.
    return '''
       B  |  I  |  N   |  G  |  O  
      {:2}  |  {} |  {}  |  {} |  {}
      {:2}  |  {} |  {}  |  {} |  {}
      {:2}  |  {} |'FREE'|  {} |  {}
      {:2}  |  {} |  {}  |  {} |  {}
      {:2}  |  {} |  {}  |  {} |  {}'''.format(card[0][0], card[0][1], card[0][2], card[0][3], card[0][4],
                                           card[1][0], card[1][1], card[1][2], card[1][3], card[1][4],
                                           card[2][0], card[2][1], card[2][3], card[2][4],
                                           card[3][0], card[3][1], card[3][2], card[3][3], card[3][4],
                                           card[4][0], card[4][1], card[4][2], card[4][3], card[4][4],)

def getCards(numPlayers, cardsPerPlayer):
    # Return x cards for x number of players.
    for i in range(numPlayers):
        for j in range(cardsPerPlayer):
            yield cards[random.randint(1, 101)]

def isWinner(board):
    # Return True if a traditional BINGO win condition has been met.
    b = board
    return ((b[0][0] == b[1][0] == b[2][0] == b[3][0] == b[4][0] == 'X') or # B column clear.
            (b[0][1] == b[1][1] == b[2][1] == b[3][1] == b[4][1] == 'X') or # I column clear.
            (b[0][2] == b[1][2] == b[3][2] == b[4][2] == 'X') or            # N column clear. Skip FREE space.
            (b[0][3] == b[1][3] == b[2][3] == b[3][3] == b[4][3] == 'X') or # G column clear.
            (b[0][4] == b[1][4] == b[2][4] == b[3][4] == b[4][4] == 'X') or # O column clear.
            (b[0][0] == b[0][1] == b[0][2] == b[0][3] == b[0][4] == 'X') or # Row 1 clear.
            (b[1][0] == b[1][1] == b[1][2] == b[1][3] == b[1][4] == 'X') or # Row 2 clear.
            (b[2][0] == b[2][1] == b[2][3] == b[2][4] == 'X') or            # Row 3 clear. Skip FREE space.
            (b[3][0] == b[3][1] == b[3][2] == b[3][3] == b[3][4] == 'X') or # Row 4 clear.
            (b[4][0] == b[4][1] == b[4][2] == b[4][3] == b[4][4] == 'X') or # Row 5 clear.
            (b[0][0] == b[1][1] == b[3][3] == b[4][4] == 'X') or            # Top-left starting diagonal clear. Skip FREE space.
            (b[4][0] == b[3][1] == b[1][3] == b[0][4] == 'X'))              # Bottom-right starting diagonal clear. Skip FREE space.


def drawBalls(drawPool):
    random.shuffle(drawPool)
    draws = []
    for i in drawPool:
        if str(i) in B:
            draws.append(f'B: {i}')
        elif str(i) in I:
            draws.append(f'I: {i}')
        elif str(i) in N:
            draws.append(f'N: {i}')
        elif str(i) in G:
            draws.append(f'G: {i}')
        elif str(i) in O:
            draws.append(f'O: {i}')

    return draws

def choosePlayers():
    numPlayers = input('Enter the number of players: (1 - 4)')
    if numPlayers not in list(str(i) for i in range(1, 5)):
        choosePlayers()
    else:
        return int(numPlayers)


def chooseCards():
    players = choosePlayers()
    print(f'You have {players} players in the game. How many cards does each player want? (1 - 25)')
    numCards = input()
    while numCards not in list(str(i) for i in range(1, 26)):
        if numCards in list(str(i) for i in range(1, 26)):
            return int(numCards)
        else:
            numCards = input('Please enter a valid number: (1 - 25)')

print(chooseCards())
#print(getBoardStr(cards[1]))

#for i in range(len(cards[1])):
#    cards[1][i][i] = 'X'
#    print(cards[1])
#    print(isWinner(cards[1]))