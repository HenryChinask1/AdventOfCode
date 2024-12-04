p = open('AdventOfCode/Advent of Code Inputs/2024day4.txt').read().split('\n')

def partOne():
    ans = 0
    for i in range(len(p)):
        for j in range(len(p[0])):
            if p[i][j] == 'X':
                # Check Left.
                if j >= 3:
                    if p[i][j - 1] == 'M':
                        if p[i][j - 2] == 'A':
                            if p[i][j - 3] == 'S':
                                #print(i, j, 'left')
                                ans += 1
                # Check right.
                if j <= (len(p[0]) - 4):
                    if p[i][j + 1] == 'M':
                        if p[i][j + 2] == 'A':
                            if p[i][j + 3] == 'S':
                                #print(i, j, 'right')
                                ans += 1
                # Check up.
                if i >= 3:
                    if p[i - 1][j] == 'M':
                        if p[i - 2][j] == 'A':
                            if p[i - 3][j] == 'S':
                                #print(i, j, 'up')
                                ans += 1
                # Check down.
                if i <= (len(p) - 4):
                    if p[i + 1][j] == 'M':
                        if p[i + 2][j] == 'A':
                            if p[i + 3][j] == 'S':
                                #print(i, j, 'down')
                                ans += 1
                # Check \ down.
                if i <= (len(p) - 4) and j <= (len(p[0]) - 4):
                    if p[i + 1][j + 1] == 'M':
                        if p[i + 2][j + 2] == 'A':
                            if p[i + 3][j + 3] == 'S':
                                #print(i, j, '\\')
                                ans += 1
                # Check \ up.
                if i >= 3 and j >= 3:
                    if p[i - 1][j -1] == 'M':
                        if p[i - 2][j - 2] == 'A':
                            if p[i - 3][j - 3] == 'S':
                                #print(i, j, '/')
                                ans += 1
                # Check / up.
                if i >= 3 and j <= (len(p[0]) - 4):
                    if p[i - 1][j + 1] == 'M':
                        if p[i - 2][j + 2] == 'A':
                            if p[i - 3][j + 3] == 'S':
                                #print(i, j, '\\ up')
                                ans += 1
                # Check / down.
                if i <= (len(p) - 4) and j >= 3:
                    if p[i + 1][j -1] == 'M':
                        if p[i + 2][j - 2] == 'A':
                            if p[i + 3][j - 3] == 'S':
                                #print(i, j, '/ down')
                                ans += 1
    print(f'Part One: {ans}')

def partTwo():
    ans = 0


partOne()
partTwo()