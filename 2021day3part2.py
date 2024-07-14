#power = open("2021day3.txt").read().split('\n')
power = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
width = len(power[0])

bitMax = []
o2Gen = 0
co2Scrub = 0

for i in range(width):
    
    zeroes = 0
    ones = 0
    for j in range(len(power)):
        if power[j][i] == '0':
            zeroes += 1
        elif power[j][i] == '1':
            ones += 1
    bitMax.append([zeroes, ones])

for i in range(bitMax):
    
for idx, byte in enumerate(power):
    power1 = power.copy()
    while len(power1) > 1:
        i = idx
        if byte[i] != max(zeroes, ones):
            power1.pop(i)
            if len(power1) == 1:
                o2Gen = int(power1[0], 2)
            else:
                i += 1

for idx, byte in enumerate(power):
    power2 = power.copy()
    while len(power2) > 1:
        if byte[idx] != min(zeroes, ones):
            power2.pop(idx)
            if len(power2) == 1:
                co2Scrub = int(power2[0], 2)



#Part two.
print(bitMax)


