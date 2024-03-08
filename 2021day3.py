power = open("2021day3.txt").read().split('\n')

gamma = ''
epsilon = ''

for i, j in enumerate(power):
    
    zeroes = 0
    ones = 0
    for j in power[i]:
        if j == '0':
            zeroes += 1
            print(gamma)
        elif j == '1':
            ones += 1
            print(epsilon)
    gamma += str(max(zeroes, ones))
    epsilon += str(min(zeroes, ones))
    




gammaDecimal = int(gamma, 2)
epsilonDecimal = int(epsilon, 2)


print(gammaDecimal * epsilonDecimal)


