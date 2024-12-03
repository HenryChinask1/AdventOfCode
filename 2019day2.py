opcodes = open('AdventOfCode/Advent of Code Inputs/2019day2.txt').read().split(',')

def checkOps(opcodes, codeZero, codeOne):
    opcodes[1] = codeZero
    opcodes[2] = codeOne
    newList = [None] * len(opcodes)
    for i in range(0, len(opcodes), 4):
        if opcodes[i] == '99':
            return newList[0:3]
        elif opcodes[i] == '1':
            opcodes[int(opcodes[i + 3])] = str(int(opcodes[int(opcodes[i + 1])]) + int(opcodes[int(opcodes[i + 2])]))
        elif opcodes[i] == '2':
            opcodes[int(opcodes[i + 3])] = str(int(opcodes[int(opcodes[i + 1])]) * int(opcodes[int(opcodes[i + 2])]))

print(f'Part One: {checkOps(opcodes, 12, 2)[0]}')

for i in range(100):
    for j in range(100):
      if checkOps(opcodes, i, j)[0] == 19690720:
          noun = checkOps(opcodes, i, j)[1]
          verb = checkOps(opcodes, i, j)[2]
          print(f'Part Two: {100 * noun + verb}')
          break

