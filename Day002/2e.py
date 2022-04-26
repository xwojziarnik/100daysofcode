"""Wczytaj plik indeksy.txt i przypisz do indexes nazwy firm zaczynających się od "WIG"""

with open("indeksy.txt", "r") as file:
    lines = file.read().splitlines()

indexes = []

for i in lines:
    if i.startswith("WIG"):
        indexes.append(i)
print(indexes)