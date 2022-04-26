"""Używając klauzuli try-except spróbuj odczytać plik."""

try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Nie znaleziono pliku.")