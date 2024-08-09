with open('Advent of Code Inputs/2015day2.txt') as f:
    boxDims = list(item.split('x') for item in f.read().split('\n'))

total = 0
total2 = 0


for box in boxDims:
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    total += (l * w * 2) + (w * h * 2) + (l * h * 2)
    total += min((l*w), (w*h), (l*h))
    total2 += min((l * 2 + w * 2), (w * 2 + h * 2), (l * 2 + h * 2))
    total2 += l * w * h

print(f'Part One: {total}')
print(f'Part Two: {total2}')
