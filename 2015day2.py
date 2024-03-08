#with open('boxSizes.txt') as f:
#    f.readlines()

boxSizes = ['3x11x24', '13x5x19', '1x9x27', '24x8x21']
dimensionL = 0
dimensionW = 0
dimensionH = 0


def l(length):
    for i in boxSizes:
        for j in i:
            if j[1] != 'x':
                sqft += int(j[0:1]) *
            length = i[
            length = int(length)
        else:
            length = int(i[0])
        dimensionL = [i] + [length]
        yield dimensionL

#def w(width):
#   for i in boxSizes:
#        if i[1] == 'x':
#            if i[3] == 'x':
#                width = i[2]
#            else:
#                width = str(i[2]) + str(i[3])
#                width = int(width)
#            dimensionW = dimensionW + [width]
#        elif i[2] == 'x':
#            if i[4] == 'x':
#                width = i[3]
#            dimensionW = dimensionW + [width]
#            else:
#                width = str(i[3]) + str(i[4])
#                width = int(width)
#            dimensionW = dimensionW + [width]


def h(height):
    for i in boxSizes:
        if i[-2] != 'x':
            height = str(i[-2]) + str(i[-1])
            height = int(height)
        else:
            height = i[-1]
    dimensionH = [i] + [height]


#for i in boxSizes:
#    totalLength = 2 *
#    totalWidth = 2 * w(boxSizes)
#    totalHeight = 2 * h(boxSizes)
#    squareFeet = totalLength + totalWidth + totalHeight
#    solution += int(squareFeet)
#    continue

l(boxSizes)
#w(boxSizes)
h(boxSizes)
print(dimensionL, dimensionW, dimensionH)
#boxSizes(squareFeet)

