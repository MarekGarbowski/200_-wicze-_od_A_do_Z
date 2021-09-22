# ćwiczenie 1

# Utwórz słownik z następujących par (klucz, wartość):
#
# 'Poland', 'Warsaw'
# 'Germany', 'Berlin'
# 'Austria', 'Vienna'
# Wynik (słownik) wydrukuj do konsoli.
# Oczekiwany wynik:
#
# {'Poland': 'Warsaw', 'Germany': 'Berlin', 'Austria': 'Vienna'}
#
#
# Uwaga:
#
# Pamiętaj, że słownik to nieuporządkowana struktura danych.
# Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

country = {'Poland': 'Warsaw',
           'Germany': 'Berlin',
           'Austria': 'Vienna'}
print(country)

# ćwiczenie 2

# capitals = {
#     'Poland': 'Warsaw',
#     'Germany': 'Berlin',
#     'Austria': 'Vienna'
# }
# Używając odpowiedniej metody wydobądź wszystkie klucze ze słownika capitals.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# dict_keys(['Poland', 'Germany', 'Austria'])

capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}

dict_keys = capitals.keys()
print(dict_keys)

# Alternatywne rozwiązanie:

capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.keys())

# ćwiczenie 3

# Podany jest słownik:
#
# capitals = {
#     'Poland': 'Warsaw',
#     'Germany': 'Berlin',
#     'Austria': 'Vienna'
# }
# Używając odpowiedniej metody wydobądź wszystkie wartości ze słownika capitals.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# dict_values(['Warsaw', 'Berlin', 'Vienna'])

capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.values())

# ćwiczenie 4

# capitals = {
#     'Poland': 'Warsaw',
#     'Germany': 'Berlin',
#     'Austria': 'Vienna'
# }
# Używając odpowiedniej metody wydobądź listę zawierającą obiekty tuple
# (klucz, wartość) ze słownika capitals. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# dict_items([('Poland', 'Warsaw'), ('Germany', 'Berlin'), ('Austria', 'Vienna')])

capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.items())

# ćwiczenie 5

# Podany jest słownik:
#
# capitals = {
#     'Poland': 'Warsaw',
#     'Germany': 'Berlin',
#     'Austria': 'Vienna'
# }
# Używając metody get() wydobądź wartość dla klucza
# 'Austria'. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# Vienna

capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}

print(capitals.get('Austria'))

# ćwiczenie 6

# Podany jest słownik:
#
# stocks = {
#     'PLW': {'Playway': 316},
#     'CDR': {'CD Projekt': 293},
#     'TEN': {'Ten Square Games': 301}
# }
# Wydobądź wartość dla klucza 'PLW'. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# {'Playway': 316}

stocks_4 = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

print(stocks_4.get('PLW'))

# Alternatywne rozwiązanie:

stocks_3 = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print(stocks_3['PLW'])

# ćwiczenie 7

# stocks = {
#     'PLW': {'Playway': 316},
#     'CDR': {'CD Projekt': 293},
#     'TEN': {'Ten Square Games': 301}
# }
# Wydobądź cenę dla spółki Ten Square Games
# (wartość dla klucza 'Ten Square Games').
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# 301

stocks_2 = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
ten = stocks_2['TEN'].values()
print(str(ten))

# Alternatywne rozwiązanie:

stocks_1 = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print(stocks_1['TEN']['Ten Square Games'])

# źwiczenie 8

# Podany jest słownik:
#
# stocks = {
#     'PLW': {'Playway': 316},
#     'CDR': {'CD Projekt': 293},
#     'TEN': {'Ten Square Games': 301}
# }
# Zaktualizuj cenę spółki CD Projekt na wartość 310.
# Wartość dla klucza 'CDR' wydrukuj do konsoli.
# Oczekiwany wynik:
#
# {'CD Projekt': 310}

stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
stocks['CDR']['CD Projekt'] = 310
print(stocks['CDR'])

# ćwiczenie 9

# Podany jest słownik:
#
# stocks = {
#     'PLW': {'Playway': 316},
#     'CDR': {'CD Projekt': 293},
#     'TEN': {'Ten Square Games': 301}
# }
# Dodaj do słownika stocks czwartą parę o kluczu: 'BBT' oraz wartości: {'Boombit': 23}.
# Wartości słownika stocks wydrukuj do konsoli.
# Oczekiwany wynik:
#
# dict_values([{'Playway': 316}, {'CD Projekt': 293}, {'Ten Square Games': 301}, {'Boombit': 23}])

stocks1 = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

stocks1['BBT'] = {'Boombit': 23}
print(stocks1.values())

# ćwiczenie 10

# Podana jest lista tickerów spółek z indeksu WIG20:
#
# ticker = [
#     'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
#     'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
#     'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
#     'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
# ]
# Przekształć tę listę w listę składającą się z dwuelementowych obiektów typu tuple (indeks, ticker).
#
#
#
# Pomocniczy wynik (sformatowany dla lepszego widoku):
#
# [(0, 'ALR'),
#  (1, 'CCC'),
#  (2, 'CDR'),
#  (3, 'CPS'),
#  (4, 'DNP'),
#  (5, 'JSW'),
#  (6, 'KGH'),
#  (7, 'LPP'),
#  (8, 'LTS'),
#  (9, 'MBK'),
#  (10, 'OPL'),
#  (11, 'PEO'),
#  (12, 'PGE'),
#  (13, 'PGN'),
#  (14, 'PKN'),
#  (15, 'PKO'),
#  (16, 'PLY'),
#  (17, 'PZU'),
#  (18, 'SPL'),
#  (19, 'TPE')]
# Oczekiwany wynik:
#
# [(0, 'ALR'), (1, 'CCC'), (2, 'CDR'), (3, 'CPS'), (4, 'DNP'), (5, 'JSW'),
# (6, 'KGH'), (7, 'LPP'), (8, 'LTS'), (9, 'MBK'), (10, 'OPL'), (11, 'PEO'),
# (12, 'PGE'), (13, 'PGN'), (14, 'PKN'), (15, 'PKO'), (16, 'PLY'), (17, 'PZU'),
# (18, 'SPL'), (19, 'TPE')]

ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]
ticker = enumerate(ticker)
print(list(ticker))

# ćwiczenie 11

# Podana jest lista tickerów spółek z indeksu WIG20:
#
# ticker = [
#     'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
#     'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
#     'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
#     'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
# ]
# Przekształć tę listę w słownik (indeks, ticker).
# Pomocniczy wynik (sformatowany dla lepszego widoku):
#
# {0: 'ALR',
#  1: 'CCC',
#  2: 'CDR',
#  3: 'CPS',
#  4: 'DNP',
#  5: 'JSW',
#  6: 'KGH',
#  7: 'LPP',
#  8: 'LTS',
#  9: 'MBK',
#  10: 'OPL',
#  11: 'PEO',
#  12: 'PGE',
#  13: 'PGN',
#  14: 'PKN',
#  15: 'PKO',
#  16: 'PLY',
#  17: 'PZU',
#  18: 'SPL',
#  19: 'TPE'}
# Oczekiwany wynik:
#
# {0: 'ALR', 1: 'CCC', 2: 'CDR', 3: 'CPS', 4: 'DNP', 5: 'JSW',
# 6: 'KGH', 7: 'LPP', 8: 'LTS', 9: 'MBK', 10: 'OPL', 11: 'PEO',
# 12: 'PGE', 13: 'PGN', 14: 'PKN', 15: 'PKO', 16: 'PLY', 17: 'PZU', 18: 'SPL', 19: 'TPE'}

ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
    ]

ticker = enumerate(ticker)
print(dict(ticker))

# ćwiczenie 12

# Podany jest słownik:
#
# project_ids = {
#     '01': 'open',
#     '03': 'in progress',
#     '05': 'in progress',
#     '04': 'completed'
# }
# Znajdź posortowaną od a do z listę unikalnych wartości, które występują w słowniku. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# ['completed', 'in progress', 'open']

project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
    }

project_ids = set(project_ids.values())
print(list(sorted(project_ids)))

# Rozwiązanie alternatywne:

project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

result = list(set(project_ids.values()))
result.sort()
print(result)

# ćwiczenie 13

# Podany jest słownik:
#
# stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
# Usuń z tego słownika parę dla klucza 'ruch'. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# {'strona': 'e-smartdata.org', 'typ': 'organiczny'}
# Uwaga:
#
# Pamiętaj, że słownik to nieuporządkowana struktura danych.
# Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
stats.pop('ruch')
print(stats)

# Rozwiązanie alternatywne:

stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
del stats['ruch']
print(stats)

# ćwicznie 14

# Podany jest słownik:
# users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
# Wydrukuj wartość dla klucza '004'
# Użyj metody, która w momencie, gdy klucz nie występuje w słowniku nie zwraca błędu
# tylko wartość domyślną. Ustaw ją na string 'nieokreślony'.

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
try:
    print(users['004'])
except KeyError:
    print('nieokreślony')

# Rozwiązanie alternatywne:

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
print(users.get('004', 'nieokreślony'))
