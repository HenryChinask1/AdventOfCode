testStrings = open('Advent of Code Inputs/2015day5.txt').read().split('\n')

firstTest = [] # Strings that contain a repeat with a buffer.
secondTest = [] # Strings that contain a pair of two letters without overlap.
finalString = []

niceStrings = 0
naughtyStrings = len(testStrings)

# Run the first check (repeat with letter in between).
for testString in testStrings:
    for i in range(len(testString) - 2):
        if testString[i] == testString[i + 2]:
            firstTest.append(testString)

firstTest = set(firstTest)
for i in firstTest:
    secondTest.append(i)

def countDict(newString):
    createList = []
    for i in range(len(newString) - 2):
        createList.append(newString[i:i + 2])
    return createList

# Run the second check (nonoverlapping pairs).
for testString in secondTest:
    currDict = countDict(testString)
    for i in currDict:
        if testString.count(i) > 1:
            finalString.append(testString)

finalString = set(finalString)

# Count the nice strings.
for i in finalString:
    niceStrings += 1

naughtyStrings = naughtyStrings - niceStrings

print(f'Nice Strings: {niceStrings}')
print(f'Naughty Strings: {naughtyStrings}')
