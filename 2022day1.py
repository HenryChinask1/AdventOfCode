C = open('calories.txt').read().split('\n\n')

calories = []

for i in C:
    calories.append(i.split('\n'))

ans = []

for i in calories:
    total = 0
    for j in i:
        total += int(j)
    ans.append(total)


x = ans.pop(ans.index(max(ans)))
y = ans.pop(ans.index(max(ans)))
z = ans.pop(ans.index(max(ans)))

part2 = int(x) + int(y) + int(z)
print(part2)
