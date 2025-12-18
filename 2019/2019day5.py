# Intcode Computer

class IntComputer:

    def __init__(self, opcodeInt):

        self.opcodeInt = opcodeInt
        self.i = 0
        self.mode1 = 0
        self.mode2 = 0
        self.mode3 = 0

    def opcodeOne(self): 
        pos1 = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        pos2 = self.i + 2 if self.mode2 else self.opcodeInt[self.i + 2]
        pos3 = self.i + 3 if self.mode3 else self.opcodeInt[self.i + 3]
        self.opcodeInt[pos3] = self.opcodeInt[pos1] + self.opcodeInt[pos2]
        self.i += 4
    
    def opcodeTwo(self):
        pos1 = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        pos2 = self.i + 2 if self.mode2 else self.opcodeInt[self.i + 2]
        pos3 = self.i + 3 if self.mode3 else self.opcodeInt[self.i + 3]
        self.opcodeInt[pos3] = self.opcodeInt[pos1] * self.opcodeInt[pos2]
        self.i += 4
    
    def opcodeThree(self):
        inputVal = input('Enter input Value (1 for Part One and 5 for Part Two): ')
        storeTo = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        self.opcodeInt[storeTo] = int(inputVal)
        self.i += 2
        
    def opcodeFour(self):
        outputVal = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        print(self.opcodeInt[outputVal])
        self.i += 2

    def opcodeFive(self):
        paramVal = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        if self.opcodeInt[paramVal]:
            newPointer = self.i + 2 if self.mode2 else self.opcodeInt[self.i + 2]
            self.i = self.opcodeInt[newPointer]
        else:
            self.i += 3

    def opcodeSix(self):
        paramVal = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        if not self.opcodeInt[paramVal]:
            newPointer = self.i + 2 if self.mode2 else self.opcodeInt[self.i + 2]
            self.i = self.opcodeInt[newPointer]
        else:
            self.i += 3

    def opcodeSeven(self):
        pos1 = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        pos2 = self.i + 2 if self.mode2 else self.opcodeInt[self.i + 2]
        pos3 = self.i + 3 if self.mode3 else self.opcodeInt[self.i + 3]
        if self.opcodeInt[pos1] < self.opcodeInt[pos2]:
            self.opcodeInt[pos3] = 1
        else:
            self.opcodeInt[pos3] = 0
        self.i += 4

    def opcodeEight(self):
        pos1 = self.i + 1 if self.mode1 else self.opcodeInt[self.i + 1]
        pos2 = self.i + 2 if self.mode2 else self.opcodeInt[self.i + 2]
        pos3 = self.i + 3 if self.mode3 else self.opcodeInt[self.i + 3]
        if self.opcodeInt[pos1] == self.opcodeInt[pos2]:
            self.opcodeInt[pos3] = 1
        else:
            self.opcodeInt[pos3] = 0
        self.i += 4

    # opcodeNinetynine.
    def hcf(self):
        print(f'Program End.')
   
    def processOpcodes(self):
        
        while True:
            turn = str(self.opcodeInt[self.i]).zfill(5)
            instruction = turn[-2:]
            self.mode1 = int(turn[2])
            self.mode2 = int(turn[1])
            self.mode3 = int(turn[0])

            if instruction == '99':
                self.hcf()
                break
            elif instruction == '01':
                self.opcodeOne()
            elif instruction == '02':
                self.opcodeTwo()
            elif instruction == '03':
                self.opcodeThree()
            elif instruction == '04':
                self.opcodeFour()
            elif instruction == '05':
                self.opcodeFive()
            elif instruction == '06':
                self.opcodeSix()
            elif instruction == '07':
                self.opcodeSeven()
            elif instruction == '08':
                self.opcodeEight()


if __name__ == '__main__':
        opcodes = [int(i) for i in open('Advent of Code Inputs/2019day5.txt').read().split(',')]
        x = IntComputer(opcodes)
        x.processOpcodes()