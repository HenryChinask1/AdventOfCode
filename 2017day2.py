spreadSheet = open('spreadsheet.txt').read().split('\n')
dataset = [i.split('\t') for i in spreadSheet]
partOne = 0
partTwo = 0

# Part One.
for i in range(len(dataset)):
    partOne += max(list(map(int, dataset[i]))) - min(list(map(int, dataset[i])))


for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        if int(dataset[i][j]) % int(dataset[j][i]) == 0:
            partTwo += int(dataset[i][j]) / int(dataset[j][i])

print(partOne)
print(partTwo)

