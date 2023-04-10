with open('class_scores.txt', 'r', encoding='utf-8') as scores, open('new_scores.txt', 'w', encoding='utf-8') as new_scores:
     for el in scores.readlines():
          print(el.split()[0] + ' ' + str(min(100, (int(el.split()[1]) + 5))), file=new_scores)
