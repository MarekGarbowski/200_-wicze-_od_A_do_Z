
# ćwiczenie 1

# Podane są dwa obiekty typu tuple:
#
# wig20 = ('CDR', 'PKO', 'PEO')
# mwig40 = ('PLW', 'AMC', 'BFT')
# Połącz te obiekty w jeden. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# ('CDR', 'PKO', 'PEO', 'PLW', 'AMC', 'BFT')

wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
stock = wig20 + mwig40
print(stock)

# ćwiczenie 2

# Podane są dwa obiekty typu tuple:
#
# wig20 = ('CDR', 'PKO', 'PEO')
# mwig40 = ('PLW', 'AMC', 'BFT')
# Zagnieźdź te obiekty w jeden obiekt typu tuple (patrz poniżej).
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# (('CDR', 'PKO', 'PEO'), ('PLW', 'AMC', 'BFT'))

wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
stock_1 = (wig20, mwig40)
print(stock_1)

# ćwiczenie 3

# Obiekty typu tuple są niemutowalne. Niech dany będzie obiekt typu tuple:
# members = (('Kasia', 23), ('Tomek', 19))
# Wstaw pomiędzy Kasię i Tomka obiekt tuple ('Adam', 26)
# tak jak pokazano poniżej. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# (('Kasia', 23), ('Adam', 26), ('Tomek', 19))

members = (('Kasia', 23), ('Tomek', 19))
members = members[0], ('Adam', 26), members[1]
print(members)

# ćwiczenenie 4

# Dany jest obiekt typu tuple:
# default = ('YES', 'NO', 'NO', 'YES', 'NO')
# Używając odpowiedniej metody zwróć liczbę wystąpień łańcucha 'YES'.
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
# Liczba wystąpień: 2

default = ('YES', 'NO', 'NO', 'YES', 'NO')
print(f'Liczba wystąpień: {default.count("YES")}')

# ćwiczenie 5

# Posortuj podany obiekt typu tuple (od A do Z):
# names = ('Monika', 'Tomek', 'Adam', 'Olaf')
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
# ('Adam', 'Monika', 'Olaf', 'Tomek')

names = ('Monika', 'Tomek', 'Adam', 'Olaf')
print(tuple(sorted(names)))

# Dany jest obiekt typu tuple:
#
# info = (('Monika', 19), ('Tomek', 21), ('Adam', 18))
# Posortuj ten obiekt (rosnąco oraz malejąco) po drugim elemencie (wiek)
# każdego zagnieżdżonego obiektu tuple.
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
#
# Oczekiwany wynik:
# Rosnąco: (('Adam', 18), ('Monika', 19), ('Tomek', 21))
# Malejąco: (('Tomek', 21), ('Monika', 19), ('Adam', 18))

info = (('Monika', 19), ('Tomek', 21), ('Adam', 18))
print(f'Rosnąco: {(tuple(sorted(info, key=lambda tup: tup[1])))}')
print(f'Malejąco: {(tuple(sorted(info, key=lambda tup: tup[1], reverse=True)))}')
print(f'Malejąco: {(tuple(sorted(info, key=lambda tup: (-tup[1]))))}')

# ćwiczenie 7

# Podany jest poniższy obiekty typu tuple:
# stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
# Wytnij trzyliterowy skrót dla spółki Playway. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# PLW

stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
stocks_1 = stocks[0]
stocks_2 = stocks_1[1]
print(stocks_2[0])

# Alternatywne rozwiązanie:

stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
print(stocks[0][1][0])

