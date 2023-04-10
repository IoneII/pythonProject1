import random as r
name = ''
book, book_rnd = [], []
for i in range(int(input())):
    name = input()
    book.append(name)
book_rnd = r.sample(book, len(book))
result = dict(zip(book, book_rnd))
print(result)

for key, value in result.items():
    while key != value:
        print(f'{key} - {value}')
        break
    else:
        book_rnd = r.sample(book, len(book))


