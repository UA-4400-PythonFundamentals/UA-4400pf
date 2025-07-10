def task(str):
    data = dict.fromkeys(str)
    for k, v in data.items():
        data[k] = str.count(k)
    return data


print(task(input('White a string: ')))
