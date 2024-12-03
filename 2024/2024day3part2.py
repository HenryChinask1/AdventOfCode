import re

p = open('AdventOfCode/Advent of Code Inputs/2024day3.txt').read()
puzzle = re.findall(r"don[']t[(][)]|do[(][)]|mul[(]\d+[,]\d+[)]", p) # add all instructions.

nums = [] # add valid instructions.
mulOn = True
for i in puzzle:
    if i.startswith("don't"):
        mulOn = False
    elif i.startswith('do()'):
        mulOn = True
    elif i.startswith('mul') and mulOn == True:
        nums.append(i)

mult = [] # parse instructions.       
for i in nums:
    mult.append(re.findall(r'\d+', i))

ans = [] # multiply instructions.
for i in mult:
    ans.append(int(i[0]) * int(i[1]))

print(sum(ans))