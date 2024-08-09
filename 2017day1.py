digitFile = str(open('Advent of Code Inputs/2017day1.txt').read().strip())
partOne = 0
partTwo = 0
digitFile2 = digitFile + digitFile
n = int(len(digitFile) / 2)

# Part one.
if digitFile[0] == digitFile[-1]:
    partOne += int(digitFile[0])

for i in range(len(digitFile) - 1):
    if int(digitFile[i]) == int(digitFile[i + 1]):
        partOne += int(digitFile[i])


# Part two.
for i in range(len(digitFile)):
    if int(digitFile2[i]) == int(digitFile2[i + n]):
        partTwo += int(digitFile2[i])


print(f'Part One: {partOne}')
print(f'Part Two: {partTwo}')