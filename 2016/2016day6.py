p = open('Advent of Code Inputs/2016day6.txt').read().split('\n')

def partOne():

    def counter(line):
        count = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in line:
            count[i] += 1
        return max(count, key=count.get)
    
    puzzle = []
    for i in range(len(p[0])):
        col = []
        for line in p:
            col.append(line[i])
        puzzle.append(col)
    message = []
    for i in puzzle:
        message.append(counter(i))

    
    print(f'Part One: {''.join(message)}')

def partTwo():
    
    def counter(line):
        count = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in line:
            count[i] += 1
        return min(count, key=count.get)
    
    puzzle = []
    for i in range(len(p[0])):
        col = []
        for line in p:
            col.append(line[i])
        puzzle.append(col)
    message = []
    for i in puzzle:
        message.append(counter(i))

    
    print(f'Part Two: {''.join(message)}')

partOne()
partTwo()