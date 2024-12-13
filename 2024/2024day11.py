p = open('AdventOfCode/Advent of Code Inputs/2024day11.txt').read().split(' ')
puzzle = []
for i in p:
    puzzle.append(int(i))


def partOne():
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

partOne()
