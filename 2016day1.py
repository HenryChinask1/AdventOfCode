import sys

movement = open('directions.txt').read().strip().split(', ')


factors = ((0, 1),  # N
           (1, 0),  # E
           (0, -1), # S
           (-1, 0)) # W

turns = {'R': lambda x : (x + 1) % 4, 'L': lambda x : (x - 1) % 4}

def main():
    currentDirection = 0 # Start facing north
    location = (0, 0)
    memo = set() # Memorize the visited locations
    for move in movement:
        d = move[0]
        c = int(move[1:])
        currentDirection = turns[d](currentDirection)
        for i in range(c):
            location = (location[0] + factors[currentDirection][0], location[1] + factors[currentDirection][1])
            if location in memo:
                print(abs(location[0]) + abs(location[1]))
                break
            memo.add(location)



if __name__ == '__main__':
    main()
