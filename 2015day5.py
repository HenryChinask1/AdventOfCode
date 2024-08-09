testStrings = open('Advent of Code Inputs/2015day5.txt').read().split('\n')

firstTest = [] # Strings that do not contain 'ab', 'cd', 'pq', or 'xy'.
secondTest = [] # Strings that contain three total vowels.
thirdTest = [] # strings that contain a double letter.


vowels = ['a', 'e', 'i', 'o', 'u']
vowelCombos = []
doubleLetters = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
notAllowed = ['ab', 'cd', 'pq', 'xy']
niceStrings = 0
naughtyStrings = len(testStrings)


# Run the first check (notAllowed strings).
for testString in testStrings:
    if notAllowed[0] not in testString and notAllowed[1] not in testString and notAllowed[2] not in testString and notAllowed[3] not in testString:
        firstTest.append(testString)

# Run the second check (three or more vowels).
for testString in firstTest:
    vowelCount = 0
    for i in testString:
        if i in vowels:
            vowelCount += 1
    if vowelCount >= 3:
        secondTest.append(testString)

# Run the third check (double letter).
for testString in secondTest:
    for i in range(len(testString) - 1):
        if testString[i:i + 2] in doubleLetters:
            thirdTest.append(testString)

thirdTest = set(thirdTest)

niceStrings = len(thirdTest)

naughtyStrings = naughtyStrings - niceStrings

print(f'Nice Strings: {niceStrings}')
print(f'Naughty Strings: {naughtyStrings}')
