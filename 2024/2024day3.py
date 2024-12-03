import re

p = open('AdventOfCode/Advent of Code Inputs/2024day3.txt').read()
puzzle = re.findall(r'mul[(]\d+[,]\d+[)]', p) # all instructions.

nums = [] # parse values.
for i in puzzle:
    nums.append(re.findall(r'\d+', i))

mult = [] # multiply values. 
for i in nums:
    mult.append(int(i[0]) * int(i[1]))

print(f'2024 Day 3 Part 1: {sum(mult)}')    