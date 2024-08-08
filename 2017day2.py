import itertools

spreadSheet = open('2017day2.txt').read().split('\n')
dataset = [i.split('\t') for i in spreadSheet]
print(dataset)
partOne = 0
partTwo = 0

# Part One.
for i in range(len(dataset)):
    partOne += max(list(map(int, dataset[i]))) - min(list(map(int, dataset[i])))

def rowCompare(lineIn):
    total = 0
    for a, b in itertools.combinations(lineIn, 2):
        if int(a) % int(b) == 0:
            total += int(a) / int(b)
        if int(b) % int(a) == 0:
            total += int(b) / int(a)
    return total

for line in dataset:
    partTwo += rowCompare(line)


print(partOne)
print(partTwo)
