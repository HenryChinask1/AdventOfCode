import copy

def partOne():
    p = open('Advent of Code Inputs/2024day11.txt').read().split(' ')
    puzzle = []
    for i in p:
        puzzle.append(int(i))

    blinks = 25
    stones = puzzle
    def stonesUpdate(stones):
        newStones = []
        for i in stones:
            if i == 0:
                newStones.append(1)
            elif len(str(i)) % 2 == 0:
                newStones.append(int(str(i)[0:len(str(i)) // 2]))
                newStones.append(int(str(i)[len(str(i)) // 2:]))
            else:
                newStones.append(i * 2024)
        return newStones
    
    while blinks:
        stones = stonesUpdate(stones)
        blinks -= 1
    
    ans = len(stones)
    print(f'Part One: {ans}')
    return stones

def partTwo():
    p = open('Advent of Code Inputs/2024day11.txt').read().split(' ')
    puzzleDict = {}
    for i in p:
        puzzleDict[int(i)] = p.count(str(i))

    # TODO: Multiply by the number of values in the dict already
    ans = 0
    puzzleDictMemo = {}
    blinks = 75
    while blinks:
        for rock, count in puzzleDict.items():
            if rock == 0:
                try:
                    puzzleDictMemo[1] += count
                except KeyError:
                    puzzleDictMemo[1] = count
                try:
                    puzzleDictMemo[rock] -= count
                except KeyError:
                    puzzleDictMemo[rock] = 0
            elif len(str(rock)) % 2 == 0:
                left = str(rock)[0: len(str(rock)) // 2]
                right = str(rock)[len(str(rock)) // 2:]
                try:
                    puzzleDictMemo[int(left)] += count
                except KeyError:
                    puzzleDictMemo[int(left)] = count
                try:
                    puzzleDictMemo[int(right)] += count
                except KeyError:
                    puzzleDictMemo[int(right)] = count
                try:
                    puzzleDictMemo[rock] -= count
                except KeyError:
                    puzzleDictMemo[rock] = 0
            else:
                try:
                    puzzleDictMemo[rock * 2024] += count
                except KeyError:
                    puzzleDictMemo[rock * 2024] = count
                try:
                    puzzleDictMemo[rock] -= count
                except KeyError:
                    puzzleDictMemo[rock] = 0
        blinks -= 1
        puzzleDict = puzzleDictMemo.copy()
    for rock, count in puzzleDictMemo.items():
        ans += count

    print(f'Part Two: {ans}')

partOne()
partTwo()
