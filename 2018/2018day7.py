steps = []

with open("Advent of Code Inputs/2018day7TEST.txt", "r") as f:
    file = f.read().split('\n')
    for i in file:
        x = i.split(' ')
        steps.append([x[1], x[-3]])

final = []

while steps:
    x = steps.pop()
    

print(steps)