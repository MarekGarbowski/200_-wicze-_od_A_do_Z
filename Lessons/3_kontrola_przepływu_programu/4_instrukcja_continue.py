
# ćwiczenie 1

# Podana jest lista spółek z indeksu WIG.GAMES wraz z ceną zamknięcia i walutą:
#
# gaming = {
#     '11B': [362.5, 'PLN'],
#     'CDR': [74.25, 'USD'],
#     'CIG': [0.85, 'PLN'],
#     'PLW': [79.5, 'USD'],
#     'TEN': [300.0, 'PLN']
# }
# Używając instrukcji continue zbuduj pętlę,
# która pozwoli zmienić cenę zamknięcia wyrażoną w USD na PLN.
# Przyjmij kurs USDPLN = 4.0.
# Słownik gaming wydrukuj do konsoli.
# Pomocniczy wynik:
# {'11B': [362.5, 'PLN'],
#  'CDR': [297.0, 'PLN'],
#  'CIG': [0.85, 'PLN'],
#  'PLW': [318.0, 'PLN'],
#  'TEN': [300.0, 'PLN']}
# Oczekiwany wynik:
# {'11B': [362.5, 'PLN'], 'CDR': [297.0, 'PLN'], 'CIG': [0.85, 'PLN'],
# 'PLW': [318.0, 'PLN'], 'TEN': [300.0, 'PLN']}

gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
    }

for k, v in gaming.items():
    if v[1] == 'PLN':
        continue
    v[0] = v[0] * 4.0
    v[1] = 'PLN'
print(gaming)

# ćwiczenie 2

# Podana jest niepełna lista imion (jednego brak):
#
# names = ['Jack', 'Leon', 'Alice', None, 'Bob']
# Posługując się instrukcją continue wydrukuj do konsoli
# tylko poprawnie przekazane imiona.
# Oczekiwany wynik:
# Jack
# Leon
# Alice
# Bob

names = ['Jack', 'Leon', 'Alice', None, 'Bob']
for name in names:
    if isinstance(name, str):
        print(name)

# Altrnatywne rozwiązanie:

names = ['Jack', 'Leon', 'Alice', None, 'Bob']
for name in names:
    if name is None:
        continue
    print(name)
