power = open("2021day3.txt").read().split('\n')
#power = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
width = len(power[0])

gamma = ''
epsilon = ''

for i in range(width):
    
    zeroes = 0
    ones = 0
    for j in range(len(power)):
        if power[j][i] == '0':
            zeroes += 1
        elif power[j][i] == '1':
            ones += 1

    if zeroes > ones:
        gamma += '0'
        epsilon += '1'

    elif ones > zeroes:
        gamma += '1'
        epsilon += '0'
    
    elif zeroes == ones:
        gamma += '1'
        epsilon += '0'

gammaDecimal = int(gamma, 2)
epsilonDecimal = int(epsilon, 2)

#Part one.
print(gammaDecimal * epsilonDecimal)


