input = open('2016day3.txt').read().split('\n')
#print(input)
possibleTriangles = []
triangles = 0

for i in input:
    possibleTriangles.append(i.split())

for i in possibleTriangles:
    if (int(i[0]) + int(i[1])) > int(i[2]):
        if (int(i[1]) + int(i[2])) > int(i[0]):
            if (int(i[2]) + int(i[0])) > int(i[1]):
                triangles += 1

print(triangles)