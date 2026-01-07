import hashlib

p = open('Advent of Code Inputs/2016day5TEST.txt').read()

def partOne():
    ans = hashlib.md5(b'abc')
    print(f'Part One: {ans.digest()}')

def partTwo():
    pass

partOne()
partTwo()