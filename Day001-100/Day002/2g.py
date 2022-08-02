"""Znajdź największą wartość wolumenu w podanym miesiącu."""

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

volumes = [line.split(',')[-1] for line in content][1:]
volumes = [int(vol) for vol in volumes]
max_vol = max(volumes)
print(f'Max Vol: {max_vol}')