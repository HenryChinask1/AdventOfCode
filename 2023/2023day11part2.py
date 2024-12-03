image = open('Advent of Code Inputs/2023day11TEST.txt').read().split('\n')
finalImage = []

# Populate the image with rows including expansion of empty rows.
for x, line in enumerate(image):
    finalImage.append(line)
    if line.find('#') == -1:
        finalImage.append(line)


# Create a list of columns that need to be expanded.
emptyColumnIndex = []
for idx in range(len(finalImage[0])):
    flag = True
    for item in range(len(finalImage)):
        if finalImage[item][idx] == '#':
            flag = False
            break
    if flag:
        emptyColumnIndex.append(idx)

print(finalImage)

# Add an empty column to the indices in emptyColumnIndex.
for idx in emptyColumnIndex[::-1]:
    for y, line in enumerate(finalImage):
        finalImage[y] = line[:idx] + '.' + line[idx:]


# Find the coordinates of the galaxies.
coordMap = []
for y, row in enumerate(finalImage):
    for x, num in enumerate(row):
        if num == '#':
            coordMap.append((x, y))

# Calculate the distance between each coordinate ((x1 - x2) + (y1 - y2)).
ans = 0
for i in coordMap:
    for j in coordMap:
        ans += ((abs(j[0]) - abs(i[0])) + (abs(j[1] - i[1])))
        
print(ans // 2)