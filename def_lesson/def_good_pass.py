s = input()

print(('NO', 'YES')[all([(any([i.isdigit() for i in s])), any([i.islower() for i in s]), any([i.isupper() for i in s]), len(s) > 6])])
