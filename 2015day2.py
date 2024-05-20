with open('boxSizes.txt') as f:
    boxDims = list(item.split('x') for item in f.read().split('\n'))

total = 0


for box in boxDims:
    l = int(box[0])
    w = int(box[1])
    h = int(box[2])
    total += (l * w * 2) + (w * h * 2) + (l * h * 2)
    total += min((l*w), (w*h), (l*h))

print(total)