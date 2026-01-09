import hashlib

p = open('Advent of Code Inputs/2016day5.txt').read()

def partOne():
    inc = 0
    ans = ''
    while len(ans) != 8:
        check = p + str(inc)
        encoded = check.encode("utf-8")
        tempAns = hashlib.md5(encoded)
        if tempAns.hexdigest()[0:5] == '00000':
            ans += tempAns.hexdigest()[5]
        inc += 1

    print(f'Part One: {ans}')

def partTwo():
    inc = 0
    ans = [0, 0, 0, 0, 0, 0, 0, 0]
    changed = [0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        check = p + str(inc)
        encoded = check.encode("utf-8")
        tempAns = hashlib.md5(encoded)
        if tempAns.hexdigest()[0:5] == '00000':
            try:
                if changed[int(tempAns.hexdigest()[5])] != 1:
                    ans[int(tempAns.hexdigest()[5])] = tempAns.hexdigest()[6]
                    changed[int(tempAns.hexdigest()[5])] = 1
            except Exception as e:
                print(e)
        if sum(changed) == 8:
            break
        inc += 1
    print(f'Part Two: {''.join(ans)}')

partOne()
partTwo()