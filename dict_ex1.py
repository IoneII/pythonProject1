params = {'sport': 'hockey', 'game': 2, 'time': 17}
params_list = []
for key in sorted(params.keys()):
    params_list.append(f'{key}={params[key]}')
    params_string = "&".join(str(i) for i in params_list)

print(params_string)