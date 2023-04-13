dict_words = dict()
words = [input() for i in range(int(input()))]
for word in sorted(words):
    dict_words[word] = sum(list(map(lambda x: ord(x) - ord('A'), word.upper())))
for el in (sorted(dict_words.items(), key=lambda word: word[1])):
    print(el[0])

