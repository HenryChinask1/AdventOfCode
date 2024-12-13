p = open('AdventOfCode/Advent of Code Inputs/2024day11.txt').read().split(' ')
puzzle = []
for i in p:
    puzzle.append(int(i))
puzzle2 = []
for i in p:
    puzzle2.append(int(i))


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

def partTwo():
    blinks = 40
    stones = puzzle2
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
        print(len(stones), blinks)
        blinks -= 1
 
    ans = len(stones)
    for _ in range(36):
        ans *= (sum([1.520618, 1.51816, 1.520884, 1.514122, 1.521279, 1.51580, 1.52061])/7)
    print(f'Part Two: {ans}')
    


partOne()
partTwo()