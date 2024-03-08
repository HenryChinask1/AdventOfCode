depth = open('depths.txt').read().split('\n')

threes = []

count = 1

for i, j in enumerate(depth[:-1]):
    threes.append((int(j) + int(depth[i+1]) + int(depth[i+2])))


# for i, j in enumerate(depth[:-1]):
#     if j < depth[i+1]:
#         count += 1


# print(count)
