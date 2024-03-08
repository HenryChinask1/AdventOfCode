digitFile = str(open('digits.txt','r').read().strip())
doubles = 0

def nextI(move):
    for i in move:
        next(i)
    return i

def addNumbers(digitFile):
    for i in digitFile:
        if i == nextI(digitFile):
            doubles += int(i)

addNumbers(digitFile)

print(digitFile[15])

print(sum(doubles))
