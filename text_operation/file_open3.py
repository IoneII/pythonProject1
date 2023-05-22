with open('logfile.txt', 'r', encoding='utf-8') as log:
     list_user = [i.strip().split() for i in log.readlines()]
     print(list_user)


     #time_user1 = list(map(lambda x: (f'{x[0].split()}  {x[1].split()} {x[2].split()} {x[3].split()}'), list_user))
     #print(time_user1)
     time_user = list(map(lambda x: x[2].split() + x[3].split(), list_user))
     print(time_user)
     for i in time_user:
          time_list = list(map(lambda x: x.split(':'), i))
          print(time_list)
          for j in time_list:
               over_hours = list(map(lambda x, y: int(x.strip(',')) * 60 + int(y.strip(',')), j))
               print(over_hours)
