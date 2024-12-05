p = open('AdventOfCode/Advent of Code Inputs/2024day5TEST.txt').read().split('\n')
pagePair = []
convert = []
books = []
incorrects = []

for i in p:
    if i == '':
        convert.append([i for i in p[p.index(i) + 1:]])
        break
    pagePair.append(i)

for i in convert[0]:
    books.append([int(i) for i in i.split(',')])

pagePairs = []
afters = {i: [] for i in range(100)}
befores = {i: [] for i in range(100)}
for i in pagePair:
    pagePairs.append([int(i) for i in i.split('|')])

for i in pagePairs:
    afters[i[0]].append(i[1])
    befores[i[1]].append(i[0])

def partOne():
    ans = 0
    checker = True
    for book in books:
        for page in book:
            for num in afters[page]:
                if num in book[0:book.index(page)]:
                    checker = False
            for num in befores[page]:
                if num in book[book.index(page):]:
                    checker = False
        if checker:
            ans += book[len(book) // 2]
        else:
            incorrects.append(book)
            checker = True
    print(f'Part One: {ans}')

def partTwo():
    def fixMids(book, befores, afters):
        return book[(len(book) // 2) + 1]
    ans = 0
    checker = True
    for book in incorrects:
        for num in afters[book[len(book) // 2]]:
            if num == book[len(book) // 2]:
                checker = False
        for num in befores[book[len(book) // 2]]:
            if num == book[len(book) // 2]:
                checker = False
    if checker:
        ans += book[len(book) // 2]
    else:
        ans += fixMids(book, befores, afters)
        checker = True
    print(f'Part Two: {ans}')

partOne()
partTwo()