from functools import reduce
with open('lines.txt', 'r', encoding='utf-8') as file:
   for stroka in file:
       for word in stroka.split():
            sum_stroka = (filter(lambda x: x.replace(x, '') if x not in ['1','2','3','4','5','6','7','8','9','0'] else int(x), word))
            print(list(sum_stroka))
       #print(sum(sum_stroka))
