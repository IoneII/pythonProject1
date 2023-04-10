import random as r
import string as s


def generate_password(length):
    rnd_list = []
    ban_set = {"l","I","1","o","0","O"}
    rnd_set = set(s.ascii_letters + s.digits) - ban_set
    LETTERS = set(s.ascii_uppercase) - ban_set
    letters = set(s.ascii_lowercase) - ban_set
    digits = set(s.digits) - ban_set
    rnd_list.append(r.choice(list(LETTERS)))
    rnd_list.append(r.choice(list(letters)))
    rnd_list.append(r.choice(list(digits)))
    rnd_list += (r.sample(rnd_set, (length - 3)))
    r.shuffle(rnd_list)
    return print(*rnd_list, sep='')

def generate_passwords(count, length):

    for _ in range(count):
        generate_password(length)

n, m = int(input()), int(input())

generate_passwords(n, m)

