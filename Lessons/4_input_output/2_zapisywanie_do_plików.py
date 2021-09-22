
# ćwiczenie 1

# Wygeneruj wszystkie liczby parzyste od 2 do 20 włącznie. Następnie zapisz każdą liczbę w osobnej linii do pliku num.txt
#
#
#
# Pomocniczo, postać pliku po rozwiązaniu zadania:
#
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18


with open('num.txt', 'w') as file:
    for number in range(1, 21):
        if number % 2 == 0:
            file.write(str(number) + '\n')

# ćwiczenie 2

# Poniższy słownik:
#
# stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
# zapisz do pliku stocks.json wykorzystując bibliotekę json.
# Użyj tzw. pretty printing ustawiając parametr wcięcia indent na wartość 4.
#
#
#
# Pomocniczo, postać pliku po rozwiązaniu zadania:
#
# {
#     "PLW": [
#         "Playway",
#         350
#     ],
#     "BBT": [
#         "Boombit",
#         22
#     ]
# }

import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)

# ćwiczenie 3

# Podane są dwie listy:
#
# headers = ['user_id', 'amount']
# users = [['001', '1400'], ['004', '1300'], ['007', '900']]
# Zapisz powyższe dane do pliku users.csv
# (plik w formacie csv - comma-separated values) tak jak pokazano poniżej.
# Zawartość pliku po zapisaniu:
#
# user_id,amount
# 001,1400
# 004,1300
# 007,900

headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]
with open('users.csv', 'w') as file:
    for id in headers:
        file.write(str(id) + ',')
    for id in users:
        file.write(str(id) + '\n')

# Rozwiązanie alternatywne:

headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('users.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')
