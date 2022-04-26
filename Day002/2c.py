"""Przy użycie try-except spróbuj wydrukować wartość dla klucza user_id. W razie błędu Keyerror zwróć poniższy tekst oraz dodaj klucz do słownika z wartością None"""

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'

try:
    print(users[user_id])
except KeyError:
    print(f"Klucz {user_id} nie występuje w słowniku. Dodawanie klucza...")
    users[user_id] = None
    print(users)