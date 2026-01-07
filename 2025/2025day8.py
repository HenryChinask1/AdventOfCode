from collections import defaultdict

def partOne():
    data = open('Advent of Code Inputs/2025day8TEST.txt').read().split('\n')
    juncPos = defaultdict(int)
    minBox = 10000000007
    maxBox = 0
    for i in data:
        adds = [int(j) for j in i.split(',')]
        juncPos[adds] = 0
        minBox = min(minBox, adds[0], adds[1], adds[2])
        maxBox = max(maxBox, adds[0], adds[1], adds[2])
    print(juncPos, minBox, maxBox)


def partTwo():
    pass

partOne()
partTwo()