s = input()
t = input()

num = list(range(len(s)))
dict_s = dict()
dict_t = dict()
flag = True
for i in range(len(s)):
    dict_s[s[i]] = num[i]
    dict_t[t[i]] = num[i]
keys_s = list(dict_s)
keys_t = list(dict_t)

print(dict_s, dict_t)
print(keys_s, keys_t)
for i in range(len(keys_s)):
        flag = False
if sum(dict_s.values()) != sum(dict_t.values()):
    flag = False
print(sum(dict_s.values()) == sum(dict_t.values()))


#  bbbaaaba
#  aaabbbba