# Intcode Computer

class IntComputer:

    def __init__(self, noun, verb, opcodeInt):

        self.noun = noun
        self.verb = verb
        self.opcodeInt = opcodeInt
        self.i = 0
        self.opcodeInt[1] = self.noun
        self.opcodeInt[2] = self.verb
        self.ans = [0, 0]

    def opcodeOne(self):

        pos1 = self.opcodeInt[self.i + 1]
        pos2 = self.opcodeInt[self.i + 2]
        pos3 = self.opcodeInt[self.i + 3]
        self.opcodeInt[pos3] = self.opcodeInt[pos1] + self.opcodeInt[pos2]
    
    def opcodeTwo(self):

        pos1 = self.opcodeInt[self.i + 1]
        pos2 = self.opcodeInt[self.i + 2]
        pos3 = self.opcodeInt[self.i + 3]
        self.opcodeInt[pos3] = self.opcodeInt[pos1] * self.opcodeInt[pos2]
    
    def hcf(self):

        if self.noun == 12 and self.verb == 2:
            print(f'Part One: {self.opcodeInt[0]}')
            self.ans[0] = 1
            if sum(self.ans) == 2:
                return

        elif self.opcodeInt[0] == 19690720:
            print(f'Part Two: {(self.noun * 100) + self.verb}')
            self.ans[1] = 1
            if sum(self.ans) == 2:
                return
            
    def processOpcodes(self):
        
        for i in range(0, len(self.opcodeInt) - 4, 4):
            self.i = i
            #print(self.opcodeInt, self.noun, self.verb)
            if self.opcodeInt[self.i] == 99:
                self.hcf()
            elif self.opcodeInt[self.i] == 1:
                self.opcodeOne()
            elif self.opcodeInt[self.i] == 2:
                self.opcodeTwo()

if __name__ == '__main__':

    for noun in range(0, 100):
        for verb in range(0, 100):
            opcodes = [int(i) for i in open('Advent of Code Inputs/2019day2.txt').read().split(',')]
            x = IntComputer(noun, verb, opcodes)
            x.processOpcodes()