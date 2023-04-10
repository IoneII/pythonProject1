import random as r
name, book = '', []
for i in range(int(input())):
    name = input()
    book.append(name)
r.shuffle(book)
for i in range(len(book)):
    print(f'{book[i-1]} - {book[i]}')
