from datetime import datetime, time

with open('diary.txt', 'r', encoding='utf-8') as file:
    text = file.read().split('\n\n')
    dict_dates = {}
    for i in range(len(text)):
        dict_dates[datetime.strptime(text[i][:17], '%d.%m.%Y; %H:%M')] = text[i][18:]

    for dt, t in sorted(dict_dates.items()):
         print(dt.strftime("%d.%m.%Y; %H:%M"), t, sep='\n')
         print()
