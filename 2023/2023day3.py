p = open('AdventOfCode/Advent of Code Inputs/2023day3.txt').read().split()

# Parse the input.
puzzle = []
for i in p:
    res = []
    for char in i:
        res.append(char)
    puzzle.append(res)

# Buff the top and bottom to not go out of range.
puzzle.append(['.'] * len(puzzle[0]))
puzzle.insert(0, ['.'] * len(puzzle[1]))

# Buff the edges to not go out of range.
for i in range(len(puzzle)):
    puzzle[i].insert(0, '.')
    puzzle[i].append('.')

def partOne():
    # For each digit in puzzle, check for a symbol in any direction.
    def checkDirs(puzzle, row, col):
        for i in [puzzle[row][col + 1], puzzle[row][col - 1], 
                  puzzle[row + 1][col], puzzle[row - 1][col], 
                  puzzle[row - 1][col - 1], puzzle[row + 1][col -1], 
                  puzzle[row + 1][col + 1], puzzle[row - 1][col + 1]]:
            if i != '.' and i.isdigit() == False:
                return True
        return False
    
    # If a digit is touching a symbol, get the full number.
    def findNum(puzzle, row, col):
        digits = []
        for i in range(col - 1, 0, -1):
            if puzzle[row][i].isdigit():
                digits.insert(0, puzzle[row][i])
            else:
                break
        for i in range(col, len(puzzle[0])):
            if puzzle[row][i].isdigit():
                digits.append(puzzle[row][i])
            else:
                break

        return int(''.join(digits))

    found = [0]
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col].isdigit():
                if checkDirs(puzzle, row, col):
                    num = findNum(puzzle, row, col)
                    if num == found[-1]:
                        continue
                    else:
                        found.append(num)

    print(f'Part One: {sum(found)}')


def partTwo():
    
    def findNum(puzzle, row, col, dir):
        digits = []
        if dir == 'left':
            row -= 1
        elif dir == 'right':
            row += 1
        elif dir == 'up':
            col -= 1
        elif dir == 'down':
            col += 1
        elif dir == 'upLeft':
            row -= 1
            col -= 1
        elif dir == 'upRight':
            row += 1
            col -= 1
        elif dir == 'dnLeft':
            row -= 1
            col += 1
        elif dir == 'dnRight':
            row += 1
            col += 1
        for i in range(col - 1, 0, -1):
            if puzzle[row][i].isdigit():
                digits.insert(0, puzzle[row][i])
            else:
                break
        for i in range(col, len(puzzle[0])):
            if puzzle[row][i].isdigit():
                digits.append(puzzle[row][i])
            else:
                break

        return int(''.join(digits))
        


    def checkGear(puzzle, row, col):
        dirs = {'left': puzzle[row - 1][col],
                'right': puzzle[row + 1][col],
                'up': puzzle[row][col - 1],
                'down': puzzle[row][col + 1],
                'upLeft': puzzle[row - 1][col - 1],
                'upRight': puzzle[row + 1][col - 1],
                'dnLeft': puzzle[row - 1][col + 1],
                'dnRight': puzzle[row + 1][col + 1]}
        gears = [0]
        for i in dirs:
            if dirs[i].isdigit():
                gear = findNum(puzzle, row, col, i)
                if gear == gears[-1]:
                    continue
                else:
                    if gear not in gears:
                        gears.append(gear)
        if len(gears) == 3:
            return gears[1] * gears[2]
        else:
            return 0

    ans = []
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == '*':
                ans.append(checkGear(puzzle, row, col))
    
    print(f'Part Two: {sum(ans)}')

partOne()
partTwo()