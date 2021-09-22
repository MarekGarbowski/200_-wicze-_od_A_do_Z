
# Korzystając z funkcji print() wydrukuj do konsoli tekst: 'Ucz się Pythona!'

print('Ucz si e Pythona!')

# Przypisz do zmiennej age wiek 20 lat (typ zmiennej int).
# Korzystając ze zmiennej age oraz funkcji print() wydrukuj do konsoli tekst:
# Mam 20 lat.

age = 20
print(f'Mam {age} lat.')

# Przypisz do zmiennej age wiek 20 lat (typ zmiennej int).
# Korzystając ze zmiennej age oraz funkcji print() wydrukuj do konsoli tekst:
# Mam 20 lat.

language = 'Python'
version = 3.8

print(f'Uczę się języka {language} w wersji {version}')

# Przypisz do zmiennej price wartość 199.99. Następnie wydrukuj do konsoli:
#
# Towar kosztuje 199.99

price = 199.99

print(f'Towar kosztuje {price}')

# Przypisz do zmiennej price wartość 69.99. Wykorzystując formatowanie f-string wydrukuj do konsoli:
#
# Towar kosztuje 69.99.

price_1 = 69.99

print(f'Towar kosztuje {price_1}.')

# 1. Przypisz dwie zmienne przechowujące cenę produktu 34.99 PLN (typ float) oraz wagę produktu 10 kg (typ int).
#
# 2. Stosując styl formatowania tekstu z poprzedniego zadania (f-string) wydrukuj do konsoli tekst:
#
# Cena: 34.99 PLN. Waga: 10 kg

price_2 = 34.99
weigh = 10
print(f'Cena: {price_2} PLN. Waga: {weigh} kg.')

# Poniżej zdefiniowane jest przybliżenie liczby pi
#
# pi = 3.1415926535
# Używając formatowania f-string wydrukuj przybliżenie liczby pi do drugiego miejsca po przecinku.
#
# Oczekiwany rezultat:
#
# Przybliżenie liczby pi do części dziesiętnych: 3.14

pi = 3.1415926535

print(f'Przybliżenie liczby pi do części dziesiętnych: {pi:.2f}')

# Używając trzech funkcji print() (jedna linia - jedna funkcja) wydrukuj poniższy tekst:
#
# ----------------------------------------
# WERSJA: 1.0.1
# ----------------------------------------

print('-' * 40)
print('WERSJA: 1.0.1')
print('-' * 40)

# Używając czterech funkcji print() (jedna linia - jedna funkcja) wydrukuj poniższy tekst:
#
# ========================================
# autor: jannowak@poczta.com
# data: 01-01-2021
# ========================================

print('=' * 40)
print('autor: jannowak@poczta.com')
print('data: 01-01-2021')
print('=' * 40)

# Używając funkcji print() oraz parametru sep ustawionego na znak '#' wydrukuj poniższy tekst:
#
# 'summer#time#holiday'

print('summer', 'time', 'holiday', sep='#')
