import string
from itertools import count
import re

count = 0
alpha = {}
ans = 0

s2 = string.ascii_letters
for i in s2:
    alpha[i] = count
    count += 1

rucks = open('sax.txt').read().split('\n')

rucktrios = [rucks[x:x+3] for x in range(0, len(rucks), 3)]

for three in rucktrios:
    for one in three:
        for letter in one:
            print(three)
            if letter in (three[0], three[1], three[2]):
                ans += alpha[letter]
    #match = re.search('/^[A-Za-z]+$/',i[0] + i[1] + i[2])
    #print(match)
    #count += alpha[match]



print(ans)
