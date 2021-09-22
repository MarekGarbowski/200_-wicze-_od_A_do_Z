
# ćwiczenie 1

# Podane są zmienne zdefiniowane poniżej:
#
# suma = 3000
# counter = 0
# Chcemy podzielić zmienną suma przez zmienną counter.
# W czasie działania pewnego programu zmienna counter może się zmieniać
# i przyjmować różne wartości.
# Używając klauzuli try: ... except: ... obsłuż wyjątek dzielenia przez zero. J
# eżeli dzielenie zostanie wykonane poprawnie wynik wydrukuj do konsoli.
# W momencie błędu do konsoli niech zostanie wydrukowany tekst:
#
# 'Dzielenie przez zero.'

suma = 3000
counter = 0

try:
    suma / counter
except ZeroDivisionError:
    print('Dzielenie przez zero.')

# Rozwiązanie alternatywne:

suma = 3000
counter = 0

try:
    result = suma / counter
    print(result)
except ZeroDivisionError:
    print('Dzielenie przez zero.')

# ćwiczenie 2

# Czasem potrzebujemy otworzyć plik o pewnej nazwie nie wiedząc
# czy taki plik istnieje.
# Zbuduj klauzulę try: ... except: ... obsługującą ten problem.
# Fragment kodu do odczytania zawartości pliku:
#
# with open('file.txt', 'r') as file:
#     content = file.read()
# Jeżeli podany plik file.txt nie istnieje wydrukuj do konsoli:
#
# Nie znaleziono pliku.

try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('Nie znaleziono pliku.')

# ćwiczenie 3

# Podany jest poniższy słownik:
#
# users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
# Spróbuj wydrukować wartość dla klucza:
#
# user_id = '004'
# W przypadku błędu KeyError wydrukuj do konsoli tekst:
#
# Klucz 004 nie występuje w słowniku. Dodawanie klucza...
# Następnie dodaj ten klucz do słownika z wartością None
# i wydrukuj słownik users do konsoli.
# Oczekiwany wynik:
# Klucz 004 nie występuje w słowniku. Dodawanie klucza...
# {'001': 'Marek', '002': 'Monika', '003': 'Jakub', '004': None}

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'
try:
    print(users[user_id])
except KeyError:
    print(f'Klucz {user_id} nie występuje w słowniku. Dodawanie klucza...')
    users[user_id] = None
print(users)