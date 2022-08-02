"""Utworzenie prostej aplikacji drukującej użytkownikowi kilka właściwości pogodowych z wybranych miejscowości
    Żródło: https://www.youtube.com/watch?v=ks6C3VWzT4M"""

from requests import get
from json import loads
from terminaltables import AsciiTable


CITIES = ['Poznań', 'Piła', 'Szczecin']


def pogodynka():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]

    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])

    table = AsciiTable(rows)
    print(table.table)


if __name__ == '__main__':
    pogodynka()
