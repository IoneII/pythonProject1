import random as r
import string as s


def generate_password(length):
    ban_set = {"l","I","1","o","0","O"}
    rnd_set = set(s.ascii_letters + s.digits) - ban_set
    rnd_list = r.sample(rnd_set, length)
    return print(*rnd_list, sep='')


def generate_passwords(count, length):

    for _ in range(count):
        generate_password(length)

n, m = int(input()), int(input())

generate_passwords(n, m)

