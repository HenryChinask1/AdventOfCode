input = open('2016day3.txt').read().split('\n')
#print(input)
sides = []
newTriangles = 0

for i in input:
    sides.append(i.split())

newSides1 = [i[0][:] for i in sides]
newSides2 = [i[1][:] for i in sides]
newSides3 = [i[2][:] for i in sides]

def triangleChecker(possibleTriangles):
    triangles = 0
    for i in possibleTriangles:
        if (int(i[0]) + int(i[1])) > int(i[2]):
            if (int(i[1]) + int(i[2])) > int(i[0]):
                if (int(i[2]) + int(i[0])) > int(i[1]):
                    triangles += 1
    return triangles

def newTriangleChecker(sideA, sideB, sideC):
    if (int(sideA) + int(sideB)) > int(sideC):
        if (int(sideB) + int(sideC)) > int(sideA):
            if (int(sideC) + int(sideA)) > int(sideB):
                return 1
    return 0

for i in range(0,len(newSides1), 3):
    newTriangles += newTriangleChecker(newSides1[i], newSides1[i + 1], newSides1[i + 2])
    newTriangles += newTriangleChecker(newSides2[i], newSides2[i + 1], newSides2[i + 2])
    newTriangles += newTriangleChecker(newSides3[i], newSides3[i + 1], newSides3[i + 2])

print(f'Part One: {triangleChecker(sides)}')
print(f'Part Two: {newTriangles}')