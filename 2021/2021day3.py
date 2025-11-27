power = open("Advent of Code Inputs/2021day3TEST.txt").read().split('\n')

def partOne():
    gamma = ''
    epsilon = ''
    for i in range(len(power[0])):
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

        elif ones >= zeroes:
            gamma += '1'
            epsilon += '0'

    gammaDecimal = int(gamma, 2)
    epsilonDecimal = int(epsilon, 2)

    print(f'Part One: {gammaDecimal * epsilonDecimal}')
    return gamma

def partTwo():
    oxRate = []
    for i in range(len(power[0])):
        zeroes = 0
        ones = 0
        for j in range(len(power)):
            if power[j][i] == '0':
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            for j in range(len(power)):
                if power[j][i] == '0':
                    oxRate.append(power[j])
    print(oxRate)

partOne()
partTwo()