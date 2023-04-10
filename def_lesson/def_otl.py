journal = []
n = int(input())
for _ in range(n):
    result = []
    for _ in range(int(input())):
        if int(input().split()[1]) > 4:
            Flag = True
        else:
            Flag = False

        result.append(Flag)
    journal.append(any(result))

print(('NO', 'YES')[all(journal)])

