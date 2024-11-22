p = 246515, 739105
valids = 0

def incCheck(num):
    for i in range(5):
        if int(num[i]) > int(num[i + 1]):
            return False
    return True

for i in range(p[0], p[1] + 1):
    i = str(i)
    for j in range(5):
        if i[j] == i[j + 1]:
            if incCheck(i):
                valids += 1
                break
            
print(valids)