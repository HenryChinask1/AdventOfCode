p = open('Advent of Code Inputs/2024day9TEST.txt').read()
puzzle = [int(i) for i in p]

def partOne():
    def parseBlocks(puzzle):
        disk = []
        currDisk = 0
        for idx, num in enumerate(puzzle):
            if idx % 2 == 0:
                for _ in range(num):
                    disk.append(currDisk)
                currDisk += 1
            elif idx % 2 != 0:
                for _ in range(num):
                    disk.append('.')
        return disk
    
    def moveFiles(fileBlock):
        moved = []
        for idx, val in enumerate(fileBlock):
            if val != '.':
                moved.append(val)
            elif val == '.':
                while fileBlock[-1] == '.':
                    fileBlock.pop()
                moved.append(fileBlock[-1])
                fileBlock.pop()
        moved.pop()
        return moved

    def updateChecksum(compressedDisk):
        checkSum = 0
        for idx, val in enumerate(compressedDisk):
                checkSum += idx * val
        return checkSum
    
    fileBlock = parseBlocks(puzzle)
    compressedDisk = moveFiles(fileBlock)
    ans = updateChecksum(compressedDisk)

    print(f'Part One: {ans}')

def partTwo():
    def parseBlocks(puzzle):
        disk = []
        currDisk = 0
        for idx, num in enumerate(puzzle):
            if idx % 2 == 0:
                for _ in range(num):
                    disk.append(currDisk)
                currDisk += 1
            elif idx % 2 != 0:
                for _ in range(num):
                    disk.append('.')
        return disk
    
    def moveFiles(fileBlock):
        moved = []
        for idx, val in enumerate(fileBlock):
            if val != '.':
                moved.append(val)
            elif val == '.':
                firstDot = idx
                lastDot = 0
                for i in fileBlock[idx:]:
                    if i != '.':
                        lastDot = fileBlock.index(i) - firstDot
                for j in range(lastDot):
                    prevNum = fileBlock[-1]
                    indices = []
                    for num in fileBlock[::-1]:
                        if num == prevNum and num != '.':
                            indices.append(num)
                        if num != prevNum or num == '.':
                            indices = []
                            break
                    if indices:
                        for i in indices:
                            moved.append(i)
        return moved
    
    def updateChecksum(compressedDisk):
        checkSum = 0
        for idx, val in enumerate(compressedDisk):
                checkSum += idx * val
        return checkSum
    
    fileBlock = parseBlocks(puzzle)
    compressedDisk = moveFiles(fileBlock)
    ans = updateChecksum(compressedDisk)

    print(f'Part Two: {ans}')

partOne()
partTwo()