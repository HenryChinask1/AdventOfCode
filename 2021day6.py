p = open('AdventOfCode/Advent of Code Inputs/2021day6TEST.txt').read().split(',')
fish = [int(i) for i in p]

def calcNewFish(fish):
    for i in range(len(fish)):
        if fish[i] > 0:
            fish[i] -= 1
        elif fish[i] == 0:
            fish[i] = 6
            fish.append(8)
    return fish

for i in range(80):
    fish = calcNewFish(fish)


print(f'Part One = {len(fish)}')