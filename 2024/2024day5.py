from copy import deepcopy

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
afters = {i: [] for i in range(11, 100)} # Keys are left side | Values cannot appear in 0:Key
befores = {i: [] for i in range(11, 100)} # Keys are right side | Values cannot appear in Key:-1
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
# Key goes before value in afters.
# Key goes after value in befores.
def partTwo():
    ans = 0
    def checkNewBook(book, befores, afters):
        for page in book:
            for num in afters[page]:
                if num in book[book.index(page):]:
                    return False
            for num in befores[page]:
                if num in book[0:book.index(page)]:
                    return False
        return True
    
    def fixMids(book, befores, afters):
        for i in range(len(book)):
            for num in afters[book[i]]:
                if num in book[book[i]:]:
                    book[book.index(num)], book[i]  = book[i], num
                    if checkNewBook(book, befores, afters):
                        return book[len(book) // 2]
                    else:
                        fixMids(book, befores, afters)
            for num in befores[book[i]]:
                if num in book[book[i]:]:
                    book[book.index(num)], book[i]  = book[i], num
                    if checkNewBook(book, befores, afters):
                        return book[len(book) // 2]
                    else:
                        fixMids(book, befores, afters)
        return book[len(book) // 2]
            # TODO: Check where the book fails.
            # TODO: Move the page to front or back depending on failure.
            # TODO: Check if the book passes.
            # TODO: Recursively fixMids until it passes and add the middle page to ans.
    
    for book in incorrects:
        print(f'The book: {book}')
        ans += fixMids(book, befores, afters)
        print(ans)
    print(f'Part Two: {ans}')

partOne()
partTwo()