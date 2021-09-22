# ćwiczenie 1

# Dana jest nazwa pliku:
#
# filename = '01012020_sales.xlsx'
# Sprawdź, czy plik jest z rozszerzeniem xlsx.
#
# Wydrukuj do konsoli 'TAK' jeśli prawda, 'NIE' jeśli fałsz.
# Oczekiwany wynik:
#
# TAK

filename = '01012020_sales.xlsx'
if filename.endswith('xlsx'):
    print('Tak')
else:
    print('Nie')

# ćwiczenie 2

# Podany jest string:
#
# code = 'DSVNDOICSN'
# Sprawdź czy zmienna code składa się tylko z dużych liter. Jeśli tak wydrukuj do konsoli 'TAK'.
# Oczekiwany wynik:
#
# TAK

code = 'DSVNDOICSN'
if code.isupper():
    print('Tak')
else:
    print('Nie')

# ćwiczenie 3

# Dana jest poniższa zmienna:
#
# number = 1.0
# Zbadaj czy zmienna jest obiektem klasy int. Wydrukuj 'TAK' jeśli prawda, 'NIE' jeśli fałsz.
# Wskazówka:
# Użyj funkcji isinstance().
# Oczekiwany wynik:
# NIE

number = 1.0
if isinstance(number, int):
    print('TAK')
else:
    print('NIE')

# ćwiczenie 4

# Podane jest poniższe hasło:
#
# password = 'cskdnjcasa#!'
# Sprawdź, czy hasło ma wymaganą długość 11 znaków.
# Jeżeli tak, wydrukuj 'Hasło poprawne', w przeciwnym razie 'Hasło zbyt krótkie'.
# Oczekiwany wynik:
#
# Hasło poprawne

password1 = 'cskdnjcasa#!'

if len(password1) >= 11:
    print('Hasło poprawne.')
else:
    print('Hasło zbyt krótkie.')

# ćwiczenie 5

# Podane jest poniższe hasło:
#
# password = 'cskdnjcasa#!'
# Sprawdź, czy hasło ma wymaganą długość 11 znaków oraz zwiera znak specjalny '!'.
# Jeżeli tak, wydrukuj 'Hasło poprawne', w przeciwnym razie 'Hasło niepoprawne'.
# Oczekiwany wynik:
# Hasło poprawne

password = 'cskdnjcasqkk#!'
if len(password) >= 11 and '!' in password:
    print('Hasło poprawne.')
else:
    print('Hasło niepoprawne')

# ćwiczenie 6

# Podana jest lista:
#
# project_ids = ['02134', '24253']
# Sprawdź czy następujące id projektu:
# project_id = '02135'
# występuje w liście project_ids. Jeśli nie dodaj id tego projektu do listy. Wydrukuj listę project_ids do konsoli.
# Oczekiwany wynik:
# ['02134', '24253', '02135']

project_ids = ['02134', '24253']
project_id = '02135'

if project_id not in project_ids:
    project_ids += [project_id]
print(project_ids)

# Rozwiązanie alternatywne:

project_ids = ['02134', '24253']
project_id = '02135'

if not project_id in project_ids:
    project_ids.append(project_id)

print(project_ids)

# ćwiczenie 7

# Dany jest słownik:
#
# project_ids = {
#     '01': 'open',
#     '02': 'new',
#     '03': 'in progress',
#     '04': 'completed'
# }
# Wykorzystując instrukcję warunkową sprawdź,
# czy status projektu z id = '02' jest ustawiony na 'new'. Jeśli tak, zmień ten status na 'open'.
#
# Wydrukuj do konsoli słownik.
# Oczekiwany wynik:
#
# {'01': 'open', '02': 'open', '03': 'in progress', '04': 'completed'}
# Uwaga:
#
# Pamiętaj, że słownik to nieuporządkowana struktura danych.
# Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if project_ids['02'] == 'new':
    project_ids['02'] = 'open'
print(project_ids)

# ćwiczenie 8

# Napisz program, który sprawdzi czy podany element:
# item = '001'
# występuje w liście:
# items = ['001', '000', '003', '005', '006']
# Jeżeli tak, to usuń ten element z listy. Wydrukuj tak otrzymaną listę do konsoli.
# Oczekiwany wynik:
# ['000', '003', '005', '006']

items = ['001', '000', '003', '005', '006']
item = '001'

if item in items:
    items.remove(item)
    print(items)

