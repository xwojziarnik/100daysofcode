"""Znajdź dzień z największą wartością wolumenu w podanym miesiacu."""

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
data = [(val[0], int(val[1])) for val in data]
max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(f'Data: {max_date}')