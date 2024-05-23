import hashlib

puzzleInput = 'iwrupvqb'
testNum = 1

while testNum < 10000000:
    testValue = puzzleInput + str(testNum)
    if len(testValue) > 4:
        res = hashlib.md5(testValue.encode())
        if res.hexdigest().startswith('00000'):
            print(f'Part 1: {testNum}')
            break
        testNum += 1

testNum = 1

while testNum < 100000000:
    testValue = puzzleInput + str(testNum)
    if len(testValue) > 5:
        res = hashlib.md5(testValue.encode())
        if res.hexdigest().startswith('000000'):
            print(f'Part 2: {testNum}')
            break
        testNum += 1
