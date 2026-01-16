compFiles = []

with open("Advent of Code Inputs/2016day9TEST.txt", "r") as f:
    file = f.read().split('\n')
    for i in file:
        compFiles.append(list(i, reversed=True))

def processMarker(chars):
    pass

for compFile in compFiles:
    length = 0
    idx = len(compFile)
    while compFile:
        curr = compFile.pop()
        length += 1
        idx -= 1
        marker = []
        if curr == '(':
            next = 0
            for i in range(9):
                if compFile[idx - i + 1] == ')':
                    next = idx - i + 1

            
            # Get the marker
        else:
            break
            # deal with the marker.


print(compFiles)