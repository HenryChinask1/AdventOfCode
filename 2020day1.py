values = open('Advent of Code Inputs/2020day1.txt').read().split('\n')
values2 = values
values3 = values

ans = 0

for i in values:
    for n in values2:
        for a in values3:
            if int(i) + int(n) + int(a) == 2020:
                ans = int(i) * int(n) * int(a)

print(f'Part Two: {ans}')
