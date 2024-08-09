depth = open('Advent of Code Inputs/2021day1.txt').read().split('\n')

threes = []

count = 0

for i, j in enumerate(depth[:-1]):
    try:
        threes.append((int(j) + int(depth[i+1]) + int(depth[i+2])))
    except:
        break



for i, j in enumerate(threes[:-1]):
    #print(j, threes[i+1])
    if j < threes[i+1]:
        count += 1


print(count)
