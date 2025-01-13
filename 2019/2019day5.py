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
    if param[0] == 0:
        if opcode[opcode[i + 1]] != 0:
            return opcode[opcode[i + 1]]
        else:
            return i + 1
    else:
        if opcode[i + 1] != 0:
            return opcode[i + 1]
        else:
            return i + 1

def opcodeSix(opcode, i, param):
    if param[0] == 0:
        if opcode[opcode[i + 1]] != 0:
            return opcode[opcode[i + 2]]
        else:
            return i + 1
    else:
        if opcode[i + 1] != 0:
            return opcode[i + 2]
        else:
            return i + 1

def opcodeSeven(opcode, i, param):
    if param[0] == 0:
        if opcode[opcode[i + 1]] < opcode[opcode[i + 2]]:
            opcode[opcode[i + 3]] = 1
        else:
            opcode[opcode[i + 3]] = 0
        return opcode
    else:
        if opcode[i + 1] < opcode[i + 2]:
            opcode[i + 3] = 1
        else:
            opcode[i + 3] = 0
        return opcode

def opcodeEight(opcode, i, param):
    if param[0] == 0:
        if opcode[opcode[i + 1]] == opcode[opcode[i + 2]]:
            opcode[opcode[i + 3]] = 1
        else:
            opcode[opcode[i + 3]] = 0
        return opcode
    else:
        if opcode[i + 1] == opcode[i + 2]:
            opcode[i + 3] = 1
        else:
            opcode[i + 3] = 0
        return opcode

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
            case '06':
                params = [(opcodes[i] // 100) % 10, (opcodes[i] //1000) % 10, (opcodes[i] // 10000) % 10]
                i = opcodeSix(opcodes, i, params)
            case '07':
                params = [(opcodes[i] // 100) % 10, (opcodes[i] //1000) % 10, (opcodes[i] // 10000) % 10]
                opcodes = opcodeSeven(opcodes, i, params)
                i += 4
            case '08':
                params = [(opcodes[i] // 100) % 10, (opcodes[i] //1000) % 10, (opcodes[i] // 10000) % 10]
                opcodes = opcodeEight(opcodes, i, params)
                i += 4
codeString()
