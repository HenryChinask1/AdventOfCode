# Intcode Computer

def opcodeOne(opcode, i, modes):
    firstVal = opcode[i + 1] if modes[0] == 0 else i + 1
    secondVal = opcode[i + 2] if modes[1] == 0 else i + 2
    thirdVal = opcode[i + 3] if modes[2] == 0 else i + 3
    opcode[thirdVal] = opcode[firstVal] + opcode[secondVal]
    return opcode
    
def opcodeTwo(opcode, i, modes):
    firstVal = opcode[i + 1] if modes[0] == 0 else i + 1
    secondVal = opcode[i + 2] if modes[1] == 0 else i + 2
    thirdVal = opcode[i + 3] if modes[2] == 0 else i + 3
    opcode[thirdVal] = opcode[firstVal] * opcode[secondVal]
    return opcode

def opcodeThree(opcode, i, param, inputVal):
    if param == 0:
        opcode[opcode[i + 1]] = inputVal
    else:
        opcode[i + 1] = inputVal
    return opcode

def opcodeFive(opcode, i, param):
    pass

def opcodeSix():
    pass

def opcodeSeven():
    pass

def opcodeEight():
    pass


def codeString():
    opcodes = [int(i) for i in open('AdventOfCode/Advent of Code Inputs/2019day5.txt').read().split(',')]
    #opcodes[1], opcodes[2] = 12, 2
    
    i = 0
    while True:
        x= str(opcodes[i]).zfill(5)
        match x[-2:]:
            case '99':
                return opcodes[0]
            case '01':
                params = [(opcodes[i] // 100) % 10, (opcodes[i] //1000) % 10, (opcodes[i] // 10000) % 10]
                opcodes = opcodeOne(opcodes, i, params)
                i += 4
            case '02':
                params = [(opcodes[i] // 100) % 10, (opcodes[i] //1000) % 10, (opcodes[i] // 10000) % 10]
                opcodes = opcodeTwo(opcodes, i, params)
                i += 4
            case '03':
                inputVal = int(input('Enter input value: '))
                param = (opcodes[i] // 100) % 10
                opcodes = opcodeThree(opcodes, i, param, inputVal)
                i += 2
            case '04':
                param = (opcodes[i] // 100) % 10
                if param == 0:
                    print(opcodes[opcodes[i + 1]])
                else:
                    print(opcodes[i + 1])
                i += 2
            case '05':
                params = [(opcodes[i] // 100) % 10, (opcodes[i] //1000) % 10, (opcodes[i] // 10000) % 10]
                i = opcodeFive(opcodes, i, params)

codeString()
