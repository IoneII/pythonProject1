def read_csv():
     with open('data.csv', 'r') as data:
          keys = [i.strip() for i in data.readline().split(',')]
          values = [value.strip().split(',') for value in data.readlines()]
          result = []
          for i in values:
               dict_list = {key: value for key, value in zip(keys, i)}
               result.append(dict_list)
          return print(result)

read_csv()