runs = open('dirs.txt').read().split('\n')
turns = []

for i in runs:
    turn = i.split(i[-2])
    turns.append(turn)

h = 0
d = 0
a = 0

for i in turns:
    if i[0] == 'forward':
        h += int(i[1])
        d += (int(i[1])*a)
    elif i[0] == 'up':
        a -= int(i[1])
        #d -= int(i[1])
    elif i[0] == 'down':
        a += int(i[1])
        #d += (int(i[1])*a)
    else:
        break



print(d * h)
