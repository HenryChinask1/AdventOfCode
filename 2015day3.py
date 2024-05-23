
santaMoves = open('santamoves.txt').read().split()

#print(santaMoves)

x = 0
y = 0

grid = [0, 0]
santaGrid = [0, 0]
roboSantaGrid = [0, 0]
houseDelivery = []
santaDelivery = []
roboSantaDelivery = []

moves = {
    'up': (0, 1),
    'down':(0, -1),
    'left': (-1, 0),
    'right': (1, 0),
}

for moves in santaMoves:
    for idx, move in enumerate(moves):
        if move == '>':
            grid = [grid[0] + 1, grid[1]]
            houseDelivery.append(grid)
        elif move == '<':
            grid = [grid[0] - 1, grid[1]]
            houseDelivery.append(grid)
        elif move == '^':
            grid = [grid[0], grid[1] + 1]
            houseDelivery.append(grid)
        elif move == 'v':
            grid = [grid[0], grid[1] - 1]
            houseDelivery.append(grid)
        if (idx + 1) % 2 != 0:
            if move == '>':
                santaGrid = [santaGrid[0] + 1, santaGrid[1]]
                santaDelivery.append(santaGrid)
            elif move == '<':
                santaGrid = [santaGrid[0] - 1, santaGrid[1]]
                santaDelivery.append(santaGrid)
            elif move == '^':
                santaGrid = [santaGrid[0], santaGrid[1] + 1]
                santaDelivery.append(santaGrid)
            elif move == 'v':
                santaGrid = [santaGrid[0], santaGrid[1] - 1]
                santaDelivery.append(santaGrid)
        else:
            if move == '>':
                roboSantaGrid = [roboSantaGrid[0] + 1, roboSantaGrid[1]]
                roboSantaDelivery.append(roboSantaGrid)
            elif move == '<':
                roboSantaGrid = [roboSantaGrid[0] - 1, roboSantaGrid[1]]
                roboSantaDelivery.append(roboSantaGrid)
            elif move == '^':
                roboSantaGrid = [roboSantaGrid[0], roboSantaGrid[1] + 1]
                roboSantaDelivery.append(roboSantaGrid)
            elif move == 'v':
                roboSantaGrid = [roboSantaGrid[0], roboSantaGrid[1] - 1]
                roboSantaDelivery.append(roboSantaGrid) 


partOneSet = []
houseSet = []

for house in houseDelivery:
    if house not in partOneSet:
        partOneSet.append(house)

print(f'Part 1: {len(partOneSet) + 1}')

for move in santaDelivery:
    if move not in houseSet:
        houseSet.append(move)

for move in roboSantaDelivery:
    if move not in houseSet:
        houseSet.append(move)


print(f'Part 2: {len(houseSet)}')