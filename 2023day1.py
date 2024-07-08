calDoc = open('calibrations.txt').read().split('\n')

numList = {'1': 'one',
           '2': 'two',
           '3': 'three',
           '4': 'four',
           '5': 'five',
           '6': 'six',
           '7': 'seven',
           '8': 'eight',
           '9': 'nine',
           '0': 'zero'}

calNums = []

for line in calDoc:
    nums = ''
    for item in line:
        if item.isdigit():
            nums += item
            break
    for item in line[::-1]:
        if item.isdigit():
            nums += item
            break
    calNums.append(nums)

ans = 0

for i in calNums:
    ans += int(i)


print(f'Part One: {ans}')