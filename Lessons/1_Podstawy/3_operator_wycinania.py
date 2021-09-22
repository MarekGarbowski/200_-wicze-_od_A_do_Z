
# ćwiczenie 1

# Z podanej nazwy pliku:
#
# filename = 'view.jpg'
# wytnij jego rozszerzenie. Wynik wydrukuj do konsoli.
#
# Oczekiwany wynik:
#
# jpg

filename = 'viev.jpg'
print(filename[-3:])

# ćwiczenie 2

# Z podanego tekstu:
#
# string = 'PKV-89415-PLN'
# wytnij kod zawierający trzy pierwsze i trzy ostatnie znaki.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# PKVPLN

string1 = 'PKV-89415-PLN'
string1 = string1[0:3] + string1[10:13]
print(string1)

# ćwiczenie 3

# Z podanego tekstu:
#
# string = '1 0 0 1 0 1'
# dzięki operatorowi wycinania usuń spacje.
# Następnie otrzymany wynik '100101' przedstaw w zapisie dziesiętnym.
# Otrzymaną liczbę wydrukuj do konsoli.
# Oczekiwany wynik:
#
# Znaleziona liczba: xx

string = '1 0 0 1 0 1'
string = string.replace(' ', '')
decimal = int(string, 2)
print(f'Znaleziona liczba: {decimal}')

# Alternatywne rozwiązanie:

string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Znaleziona liczba: {number}')

# ćwiczenie 4

# Posługując się operatorem wycinania, odwróć kolejność znaków w poniższym tekście:
# text = 'Kurs Python'
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# nohtyP sruK

text = 'Kurs Python'
print(text[::-1])
