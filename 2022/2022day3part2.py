import string
from itertools import count
import re

values = 1
alpha = {}
ans = 0

s2 = string.ascii_letters
for i in s2:
    alpha[i] = values
    values += 1

rucks = open('Advent of Code Inputs/2022day3.txt').read().split('\n')

rucktrios = [rucks[x:x+3] for x in range(0, len(rucks), 3)]
#print(rucktrios)


for rux in rucktrios:
    #print(rux)
    for letter in rux[0]:
        if rux[1].count(letter) >= 1 and rux[2].count(letter) >= 1:
            ans += alpha[letter] / rux[0].count(letter)
            #print(ans)




print(int(round(ans)))
