func =  lambda x: True if x[0].lower() == x[-1].lower() == 'a' else False
print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))

