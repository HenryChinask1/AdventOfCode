import itertools

testStrings = open('nice_naughty.txt').read().split('\n')

firstTest = []
secondTest = []
thirdTest = []


vowels = ['a', 'e', 'i', 'o', 'u']
vowelCombos = []
doubleLetters = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
notAllowed = ['ab', 'cd', 'pq', 'xy']
niceStrings = 0
naughtyStrings = 0

for i in itertools.product(vowels, repeat=3):
    
    vowelCombos.append(i)

print(vowelCombos)

for testString in testStrings:
    if notAllowed[0] not in testString and notAllowed[1] not in testString and notAllowed[2] not in testString and notAllowed[3] not in testString:
        firstTest.append(testString)

for testString in firstTest:
    for inclusion in doubleLetters:
        if inclusion in testString:
            secondTest.append(testString)

for word in secondTest:
    newWord = ''
    for idx, letter in enumerate(word):
        if letter in 'aeiou':
            newWord += letter
        if idx == 15:
            thirdTest.append(newWord)

for word in thirdTest:
    if len(word) < 3:
        continue
    #if word in 



'''
for inclusion in vowelCombos:
    for testString in secondTest:
        if inclusion[0] in testString:
            newTest = testString.replace(inclusion[0], '', 1)
        if inclusion[1] in newTest:
            newTest2 = newTest.replace(inclusion[1], '', 1)
        if inclusion[2] in newTest2:
            thirdTest.append(newTest2)
            niceStrings += 1
'''
#print(len(secondTest))
#print(len(thirdTest))
print(f'Nice Strings: {niceStrings}')
print(f'Naughty Strings: {naughtyStrings}')
