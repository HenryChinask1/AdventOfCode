# Password Check

p = 246515, 739105
validsPartOne = 0
validsPartTwo = 0

def incCheck(num):
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return False
    return True

def doubleCheck(num):
    count = 1
    currNum = num[0]
    for i in range(1, len(num)):
        if num[i] == currNum:
            count += 1
        else:
            if count == 2:
                return True
            else:
                currNum = num[i]
                count = 1
    if count == 2:
        return True
    return False

for i in range(p[0], p[1] + 1):
    i = str(i)
    for j in range(5):
        if i[j] == i[j + 1]:
            if incCheck(i):
                validsPartOne += 1
                break

for i in range(p[0], p[1] + 1):
    if doubleCheck(str(i)) and incCheck(str(i)):
        validsPartTwo += 1

print(f'Part One: {validsPartOne}')
print(f'Part Two: {validsPartTwo}')


