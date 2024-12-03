calDoc = open('Advent of Code Inputs/2023day1.txt').read().split('\n')

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