opcodes = open('Advent of Code Inputs/2019day2.txt').read().split(',')
opcodes[1] = '12'
opcodes[2] = '2'

for i in range(0, len(opcodes), 4):
    if opcodes[i] == '99':
        break
    elif opcodes[i] == '1':
        opcodes[int(opcodes[i + 3])] = str(int(opcodes[int(opcodes[i + 1])]) + int(opcodes[int(opcodes[i + 2])]))
    elif opcodes[i] == '2':
        opcodes[int(opcodes[i + 3])] = str(int(opcodes[int(opcodes[i + 1])]) * int(opcodes[int(opcodes[i + 2])]))

print(f'Part One: {opcodes[0]}')