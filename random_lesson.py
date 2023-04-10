import random as r
import string as s

def generate_index():

    return print((f'{s.ascii_uppercase[r.randrange(26)]}{s.ascii_uppercase[r.randrange(26)]}'
                  f'{str(r.randrange(100))}_{str(r.randrange(100))}{s.ascii_uppercase[r.randrange(26)]}'
                  f'{s.ascii_uppercase[r.randrange(26)]}'))

generate_index()

