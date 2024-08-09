input = open('Advent of Code Inputs/2015day7.txt').read().split('\n')

circuits = []

for i in input:
    circuits.append(i.split(' '))

def Sort(circuits):
    l = len(circuits)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (circuits[j][-1] > circuits[j + 1][-1]):
                tempo = circuits[j]
                circuits[j] = circuits[j + 1]
                circuits[j + 1] = tempo
    
    return circuits

puzzleInput = Sort(circuits)
circuits.sort(key=len)
print(puzzleInput)