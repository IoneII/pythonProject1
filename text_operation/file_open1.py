import time
start = time.time()
with open('lines.txt', 'r', encoding='utf-8') as file:
    count_lines = len(file.readlines())
    file.seek(0)
    count_letters = sum([len(word.strip('.,?"!-:1234567890')) for word in file.read().split()])
    file.seek(0)
    count_words = len([word for word in file.read().split()])

print(f'Input file contains:\n{count_letters} letters\n{count_words} words\n{count_lines} lines')
end = time.time()
print(end - start)