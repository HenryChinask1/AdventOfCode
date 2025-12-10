# Password Check
import re

class PasswordCheck:

    def __init__(self, low, hi):
        self.low = low
        self.hi = hi
        self.num = str(low)
        self.validsOne = 0
        self.validsTwo = 0
        self.checked = set()

    def incCheck(self):
        for i in range(len(self.num) - 1):
            if int(self.num[i]) > int(self.num[i + 1]):
                return False
        return True
    
    def doubleCheck(self):
        count = 1
        currNum = self.num[0]
        for i in range(1, len(self.num)):
            if self.num[i] == currNum:
                count += 1
            else:
                if count == 2:
                    return True
                else:
                    currNum = self.num[i]
                    count = 1
        if count == 2:
            return True
        return False
    
    def checkValidsOne(self):
        for i in range(self.low, self.hi + 1):
            self.num = str(i)
            for j in range(5):
                if self.num[j] == self.num[j + 1]:
                    if self.incCheck():
                        self.validsOne += 1
                        self.checked.add(i)
                        break
    
    def checkValidsTwo(self):
        for i in range(self.low, self.hi + 1):
            self.num = str(i)
            if self.doubleCheck() and self.incCheck():
                self.validsTwo += 1
                self.checked.add(i)

if __name__ == '__main__':
    data = re.findall(r'\d+', open('Advent of Code Inputs/2019day4.txt').read())
    low = int(data[0])
    hi = int(data[1])
    x = PasswordCheck(low, hi)
    x.checkValidsOne()
    x.checkValidsTwo()
    print(f'Part One: {x.validsOne}')
    print(f'Part Two: {x.validsTwo}')
    print(len(x.checked))
