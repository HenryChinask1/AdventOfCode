file = open('2018day4TEST.txt').read().split('\n')
guardTimes = []

for i in file:
    word = i.split(' ')
    guardTimes.append([' '.join(word[i:i + 2]) for i in range(0, len(word), 2)])

print(guardTimes)