import re
import string
from itertools import count

count = 1
rucks = open('Advent of Code Inputs/2022day3.txt').read().split('\n')
alpha = {}
ans = 0.0

s2 = string.ascii_letters
for i in s2:
    alpha[i] = count
    count += 1
#print(alpha)

for i in rucks:
    lefts = i[0:len(i) // 2]
    rights = i[len(i) // 2:]
    #print([lefts, rights])
    for letter in lefts:
        if rights.count(letter) >= 1:
            ans += alpha[letter] / lefts.count(letter)


print(int(round(ans)))


