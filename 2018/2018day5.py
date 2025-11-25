
# Parse input.
data = open('Advent Of Code Inputs/2018day5.txt').read()
elems = []

for i in data:
    elems.append(i)

# Create a stack with the units, popping off matches along the way.
def partOne(part):
    newPart = []
    i = 0

    while i < len(part):
        if newPart and abs(ord(part[i]) - ord(newPart[-1])) == 32:
            newPart.pop()
            i += 1
        else:
            newPart.append(part[i])
            i += 1
    return newPart

# Create the shortest polymer by removing each type of element.
def partTwo():
    alpha = ['aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH', 'iI', 'jJ', 'kK', 'lL', 'Mm', 'nN', 'oO', 'pP', 'Qq', 'rR', 'sS', 'tT', 'uU', 'vV', 'wW', 'xX', 'yY', 'zZ']
    ans = len(elems)

    for i in alpha:
        newElems = [j for j in elems if j not in i]

        newPart = []
        x = 0
        while x < len(newElems):
            if newPart and abs(ord(newElems[x]) - ord(newPart[-1])) == 32:
                newPart.pop()
                x += 1
            else:
                newPart.append(newElems[x])
                x += 1
        ans = min(ans, len(newPart))
    return ans

ans = partOne(elems)
ans2 = partTwo()
print(f'Part One: {len(ans)}')
print(f'Part Two: {ans2}')