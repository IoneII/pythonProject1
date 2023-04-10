client = dict()

for _ in range(int(input())):
    name, item, count = input().split()
    if name not in client.keys():
        client[name] = client.setdefault(name, {item: count})
    else:
        if item not in client[name]:
            client[name].update({item: count})
        else:
            client[name][item] = int(client[name].get(item)) + int(count)


for k, v in sorted(client.items()):
    print(k, ":")
    for key, value in client[k].items():
        print(key, value)
