# ćwiczenie 1

# Napisz program, który znajdzie wszystkie liczby dwucyfrowe podzielne przez 11.
# Wynik wydrukuj do konsoli w postaci wartości rozdzielonych przecinkiem.
# Oczekiwany wynik:
# 11,22,33,44,55,66,77,88,99

digits = []
for digit in range(1, 100):
    if digit % 11 == 0:
        digits.append(str(digit))
print(','.join(digits))

# Alternatywne rozwiązanie:

result = []
for i in range(10, 100):
    if i % 11 == 0:
        result.append(str(i))
print(','.join(result))

# ćwiczenie 2

# Napisz program, który znajdzie wszystkie liczby dwucyfrowe podzielne przez 11
# oraz niepodzielne przez 3. Wynik wydrukuj do konsoli w postaci wartości rozdzielonych przecinkiem.
# Oczekiwany wynik:
# 11,22,44,55,77,88

digits1 = []

for digit in range(1, 100):
    if digit % 11 == 0 and digit % 3 != 0:
        digits1.append(str(digit))
print(','.join(digits1))

# ćwiczenie 2

# Podana jest lista liczb:
# items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
# Napisz program, który usunie liczby nieparzyste i zwróci pozostałe. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# [4, 6, 10, 24]

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
even_numbers = []
for item in items:
    if item % 2 == 0:
        even_numbers.append(item)
print(even_numbers)

# ćwiczenie 4

# Podana jest lista:
# items = [1, 5, 3, 2, 2, 4, 2, 4]
# Napisz program, który usunie duplikaty z listy (kolejność musi zostać zachowana).
# Oczekiwany wynik:
#
# [1, 5, 3, 2, 4]

items = [1, 5, 3, 2, 2, 4, 2, 4]
items2 = []
for item in items:
    if item in items2:
        continue
    items2.append(item)

print(items2)

# Alternatywne rozwiazanie:

items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

for item in items:
    if not item in result:
        result.append(item)

print(result)

# ćwiczenie 5

# Napisz program, który z podanego tekstu:
#
# text = 'Python jest bardzo popularnym językiem programowania'
# wytnie dokładnie cztery pierwsze wyrazy.
# Przeprowadź standaryzację każdego wyrazu, tzn. zamień duże litery na małe.
# Wynik przedstaw w postaci listy i wydrukuj do konsoli.
# Oczekiwany wynik:
#
# ['python', 'jest', 'bardzo', 'popularnym']

text = 'Python jest bardzo popularnym językiem programowania'
text_cut = []
text = text.lower()
text = text.split()
print(text)
for index, word in enumerate(text):
    if index < 4:
        text_cut.append(word.lower())
print(text_cut)

# ćwiczenie 6

# Napisz program, który z podanej listy zwróci listę wartości
# powyżej ustalonego progu 0.5:
# probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
# Oczekiwany wynik:
#
# [0.91, 0.55, 0.76]

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
for digit in probabilities:
    if digit > 0.5:
        result.append(digit)
print(result)

# ćwiczenie 7

# Rozważmy problem klasyfikacji binarnej.
# Model uczenia maszynowego zwraca prawdopodobieństwo przynależności do klasy.
# Jeżeli jest ono mniejsze od 0.5 próbka zostaje przypisana do klasy 0,
# przeciwnie do klasy 1.
#
# Podana jest lista prawdopodobieństw trzymanych z modelu uczenia maszynowego:
#
# probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
# Napisz program, który przypisze klasę 0 dla wartości mniejszych od 0.5 oraz 1
# dla wartości większych lub równych 0.5.
# Wynik w postaci listy wydrukuj do konsoli.
# Oczekiwany wynik:
# [0, 1, 0, 1, 1, 0]

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
for digit in probabilities:
    if digit < 0.5:
        result.append(0)
    else:
        result.append(1)
print(result)

# ćwiczenie 8

# Napisz program, który utworzy histogram -
# rozkład częstości w postaci słownika z podanych wartości:
# items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
# Oczekiwany wynik:
# {'x': 3, 'y': 4, 'z': 2}
# Uwaga:
# Pamiętaj, że słownik to nieuporządkowana struktura danych.
# Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
result = {}
for digit in items:
    if digit == 'x':
        result['x'] = result.get('x', 0) + 1
    elif digit == 'y':
        result['y'] = result.get('y', 0) + 1
    elif digit == 'z':
        result['z'] = result.get('z', 0) + 1
print(result)

# Alternatywne rozwiązanie:

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1

print(freq)

# ćwiczenie 9

# Podany jest tekst:
#
# text = """Python – język programowania wysokiego poziomu
# ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
# standardowych, którego ideą przewodnią jest czytelność i
# klarowność kodu źródłowego."""
# Utwórz listę słów z podanego tekstu.
# Następnie dokonaj standaryzacji (zamień duże litery na małe, usuń znaki interpunkcyjne).
# Odfiltruj tylko wyrazy z długością powyżej 10 znaków. Otrzymaną listę wydrukuj do konsoli:
# Oczekiwany wynik:
#
# ['programowania', 'przeznaczenia', 'rozbudowanym', 'standardowych']

text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""

text = text.lower().replace('.', '').replace(',', '').split()
result = []
for word in text:
    if len(word) > 10:
        result.append(word)
print(result)

# Rozwiązanie alternatywne:

text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""

words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 10]
print(words)

# ćwiczenie 10

# indexes = [
#     'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE',
#     'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
#     'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
#     'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
#     'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
#     'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
#     'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
#     'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
# ]
# Dokonaj iteracji po liście indexes oraz wydrukuj do konsoli tylko te indeksy
# zwierające w nazwie '20' lub '30'.
# Oczekiwany wynik:
#
# WIG20
# WIG20dvp
# WIG20lev
# WIG20short
# WIG20TR
# WIG30
# WIG30TR

indexes = [
    'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE',
    'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
    'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
    'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
    'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
    'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
    'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
    'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
    ]

for index in indexes:
    if '20' in index or '30' in index:
        print(index)

# ćwiczenie 11

# Podany jest słownik spółek z indeksu sektorowego WIG.GAMES. Kluczem jest 3-literowy kod spółki, wartością cena zamknięcia:
#
# gaming = {
#     '11B': 362.5,
#     'CDR': 297.0,
#     'CIG': 0.85,
#     'PLW': 318.0,
#     'TEN': 300.0
# }
# Przeprowadź iterację po słowniku.
# Wydrukuj kody tych spółek, których cena zamknięcia jest większa niż 100.00 PLN.
# Oczekiwany wynik:
# 11B
# CDR
# PLW
# TEN

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
    }

for c, p in gaming.items():
    if p > 100:
        print(c)

# ćwiczenie 12

# Podana jest lista imion wprowadzonych do systemu przez użytkowników (bez procesu walidacji):
#
# names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
# Sprawdź, czy każde imię jest poprawne (składa się tylko z liter).
# Jeżeli tak, wynik wydrukuj do konsoli w następującej postaci, np. Hello Jack!
# Wskazówka:
# Użyj metody str.isalpha()
# Oczekiwany wynik:
# Hello Jack!
# Hello Leon!
# Hello Alice!
# Hello Bob!

names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
for name in names:
    if name.isalpha():
        print(f'Hello {name}')

