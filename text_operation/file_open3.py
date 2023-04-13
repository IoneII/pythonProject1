with open('logfile.txt', 'r', encoding='utf-8') as log, open('output.txt', 'w', encoding='utf-8') as out:
     list_user = [i.strip().split() for i in log.readlines()]
     time_user = list(map(lambda x: x[2].strip(',').split() + x[3].split(), list_user))
     result = []
     for i in time_user:
          time_list1 = list(map(int, list(map(lambda x: x.split(':'), i))[0]))
          time_list2 = list(map(int, list(map(lambda x: x.split(':'), i))[1]))
          over_hour = (time_list1[0]*60 + time_list1[1]) - (time_list2[0]*60 + time_list2[1])
          result.append(over_hour)
     for i in range(len(result)):
          if abs(result[i]) >= 60:
               print(list_user[i][0] + ' ' + list_user[i][1].strip(','), file=out, sep='')

