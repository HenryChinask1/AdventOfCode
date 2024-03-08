rounds = open('rps.txt').read().split('\n')

#Rock Paper Scissors
import random, sys

print('Rock, Paper, Scissors')

#These variables keep track of wins, losses, and draws
wins = 0
losses = 0
draws = 0
rocks = 0
papers = 0
scissors = 0

#while True: #The main game loop
for i in rounds:
    #print('%s Wins, %s Losses, %s Draws' % (wins, losses, draws))
    #while True:#The player input loop
        #print('Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit')
    playerMove = i[2]
    if playerMove == 'X':
        if i[0] == 'A':
            playerMove = 'C'
            scissors += 3
        if i[0] == 'B':
            playerMove = 'A'
            rocks += 1
        if i[0] == 'C':
            playerMove = 'B'
            papers += 2
    if playerMove == 'Y':
        if i[0] == 'A':
            playerMove = 'A'
            rocks += 1
        if i[0] == 'B':
            playerMove = 'B'
            papers += 2
        if i[0] == 'C':
            playerMove = 'C'
            scissors += 3
    if playerMove == 'Z':
        if i[0] == 'A':
            playerMove = 'B'
            papers += 2
        if i[0] == 'B':
            playerMove = 'C'
            scissors += 3
        if i[0] == 'C':
            playerMove = 'A'
            rocks += 1
           # sys.exit() #Quit the game
        #if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
       #     break # Break out of the player move loop
       # print('Type r, p, s, or q')

    # Display what player chose
    #if playerMove == 'r':
    #    print('Rock versus...')
    #elif playerMove == 'p':
    #    print('Paper versus...')
    #elif playerMove == 's':
    #    print('Scissors versus...')

    #Display what computer chose
    computerMove = i[0]
#     if computerMove == 'A':
#         computerMove = 'X'
#     if computerMove == 'B':
#         computerMove = 'Y'
#     if computerMove == 'C':
#         computerMove = 'Z'
#     if randomNumber == 1:
#        computerMove = 'r'
#        print('ROCK')
#     elif randomNumber == 2:
#        computerMove = 'p'
#        print('PAPER')
#     elif randomNumber == 3:
#        computerMove = 's'
#        print('SCISSORS')

    #Display and record win/loss/draw
    if playerMove == computerMove:
        print('It is a draw!')
        draws = draws + 3
    elif playerMove == 'A' and computerMove == 'C':
        print('YOU WIN!')
        wins = wins + 6
    elif playerMove == 'B' and computerMove == 'A':
        print('YOU WIN')
        wins = wins + 6
    elif playerMove == 'C' and computerMove == 'B':
        print('YOU WIN!')
        wins = wins + 6
    elif playerMove == 'A' and computerMove == 'B':
        print('YOU LOSE')
        losses = losses + 0
    elif playerMove == 'B' and computerMove == 'C':
        print('YOU LOSE')
        losses = losses + 0
    elif playerMove == 'C' and computerMove == 'A':
        print('YOU LOSE')
        losses = losses + 0


print(wins + losses + draws + rocks + papers + scissors)
