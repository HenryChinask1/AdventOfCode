p = open('AdventOfCode/Advent of Code Inputs/2024day9TEST.txt').read()
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
        return disk, len(disk)
    
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
        return moved
    
    def updateChecksum(compressedDisk, diskSize):
        for _ in range(diskSize - len(compressedDisk)):
            compressedDisk.append('.')
        checkSum = 0
        for idx, val in enumerate(compressedDisk):
            if val == '.':
                checkSum += idx
            else:
                checkSum += idx * val
        return checkSum
    
    fileBlock, diskSize = parseBlocks(puzzle)
    compressedDisk = moveFiles(fileBlock)
    ans = updateChecksum(compressedDisk, diskSize)

    print(f'Part One: {ans}')
    #print(f'6415449222092 is not the answer')
    #print(f'6415449267161 is not the answer')
    #print(f'6418726729910 is not the answer')


def partTwo():
    pass

partOne()
partTwo()