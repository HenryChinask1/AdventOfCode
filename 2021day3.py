power = open('power.txt')

zeroes = 0
ones = 0
n = 0
gamma = ''
epsilon = ''
ans = []

def

for i, j in enumerate(power, start = 1):
    if j[n] == '0':
        zeroes += 1
        if n == 12:
            break
        else:
            n += 1
            continue
    elif j[n] == '1':
        ones += 1
        if n == 12:
            break
        else:
            n += 1
            continue

#         if j[n] == '0':
#             zeroes += 1
#         if j[n] == '1':
#             ones += 1
#     if zeroes > ones:
#         gamma += '0'
#         epsilon += '1'
#     else:
#         gamma += '1'
#         epsilon += '0'
#     zeroes = 0
#     ones = 0

# ans = int(gamma, 2) * int(epsilon, 2)

# print(gamma)

