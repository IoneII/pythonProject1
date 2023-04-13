from functools import reduce
import pysnooper

@pysnooper.snoop()

def hide_card(card_number):
    return '*' * 12 + str(reduce(lambda x, y: x + y, [i for i in card_number.split()]))[-4:]

print(hide_card('1034 3948 1944 6327'))