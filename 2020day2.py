passwords = open('password.txt').read().split('\n')
password1 = []

for i in passwords:
    password1.append(i.split())

for j, v in enumerate(password1[0].split('-')):
    print(j,v)



#print(password1)
