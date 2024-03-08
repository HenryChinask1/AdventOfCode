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
        rocks += 1
    if playerMove == 'Y':
        papers += 2
    if playerMove == 'Z':
        scissors += 3
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
    if computerMove == 'A':
        computerMove = 'X'
    if computerMove == 'B':
        computerMove = 'Y'
    if computerMove == 'C':
        computerMove = 'Z'
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
    elif playerMove == 'X' and computerMove == 'Z':
        print('YOU WIN!')
        wins = wins + 6
    elif playerMove == 'Y' and computerMove == 'X':
        print('YOU WIN')
        wins = wins + 6
    elif playerMove == 'Z' and computerMove == 'Y':
        print('YOU WIN!')
        wins = wins + 6
    elif playerMove == 'X' and computerMove == 'Y':
        print('YOU LOSE')
        losses = losses + 0
    elif playerMove == 'Y' and computerMove == 'Z':
        print('YOU LOSE')
        losses = losses + 0
    elif playerMove == 'Z' and computerMove == 'X':
        print('YOU LOSE')
        losses = losses + 0


print(wins + losses + draws + rocks + papers + scissors)
