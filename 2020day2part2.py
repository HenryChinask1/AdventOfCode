passwords = open('password.txt').read().split('\n')
password1 = [] # The test character is i[1[0]], test string is i[2]

okPasswords = 0

for i in passwords:
    password1.append(i.split(' '))

minMax = []
minsMaxs = [] # Two nums, a min and max amount of chars allowed.

for i in password1:
    minMax.append(i[0])

for i in minMax:
    minsMaxs.append(i.split('-'))


for idx, password in enumerate(password1):
    if len(password[2][int()]):
        if password[2][int(minsMaxs[idx][0])+1] == password[1][0]:
            okPasswords += 1
        if password[2][int(minsMaxs[idx][1])+1] == password[1][0]:
            okPasswords += 1
        
print(okPasswords)
