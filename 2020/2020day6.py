puzzle = open('AdventOfCode/Advent of Code Inputs/2020day6.txt').read().split('\n\n')

ans = 0

for i in range(len(puzzle)):
    puzzle[i] = puzzle[i].replace('\n', '')
    ans += len(set(puzzle[i]))

print(ans)