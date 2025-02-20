p = open('AdventOfCode/Advent of Code Inputs/2017day6.txt').read()

def partOne(steps, ans, puzzle):
    for _ in range(10000):
        moveMemory = max(puzzle)
        idx = puzzle.index(max(puzzle))
        puzzle[idx] = 0
        while moveMemory:
            if idx < len(puzzle) - 1:
                idx += 1
            else:
                idx = 0
            puzzle[idx] += 1
            moveMemory -= 1
        steps += 1
        compare = tuple(puzzle)
        if len(ans) != len(set(ans)):
            return steps - 1
        else:
            ans.append(compare)
    return None

def partTwo():
    pass

print(f'Part One: {partOne(steps=0, ans=[], puzzle=[int(i) for i in p.split()])}')
partTwo()