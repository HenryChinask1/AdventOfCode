# Intcode Computer

def intComputer(noun, verb):
    opcodes = [int(i) for i in open('AdventOfCode/Advent of Code Inputs/2019day2.txt').read().split(',')]
    opcodes[1], opcodes[2] = noun, verb

    def opcodeOne(opcode, i):
        opcode[opcode[i + 3]] = opcode[opcode[i + 1]] + opcode[opcode[i + 2]]
        return opcode

    def opcodeTwo(opcode, i):
        opcode[opcode[i + 3]] = opcode[opcode[i + 1]] * opcode[opcode[i + 2]]
        return opcode

    for i in range(0, len(opcodes) - 4, 4):
        if opcodes[i] == 99:
            if (noun, verb) == (12, 2):
                print(f'Part One: {opcodes[0]}')
            if opcodes[0] == 19690720:
                print(f'Part Two: {(100 * noun) + verb}')
        if opcodes[i] == 1:
            opcodes = opcodeOne(opcodes, i)
        if opcodes[i] == 2:
            opcodes = opcodeTwo(opcodes, i)


for noun in range(1, 100):
    for verb in range(1, 100):
        intComputer(noun, verb)