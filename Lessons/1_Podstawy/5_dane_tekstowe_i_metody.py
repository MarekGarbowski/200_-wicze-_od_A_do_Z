
# ćwiczenie 1

# Dany jest tekst:
#
# text = 'python jest popularnym językiem programowania.'
# Używając odpowiedniej metody zamień pierwszą literę tekstu na dużą.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# Python jest popularnym językiem programowania.

text = 'python jest popularnym językiem programowania.'
print(text.capitalize())

# ćwiczenie 2

# Dany jest tekst:
#
# text = 'python jest popularnym językiem programowania.'
# Używając odpowiedniej metody zlicz liczbę wystąpień litery 'p'.
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.

# Oczekiwany wynik:
#
# Liczba wystąpień: 4

text = 'python jest popularnym językiem programowania.'
print(f'Liczba wystąpień: {text.count("p")} ')

# ćwiczenie 3

# Dane są poniższe kody:
#
# code1 = 'FVNISJND-XX-2020'
# code2 = 'FVNISJND-XY-2019'
# Używając odpowiedniej metody sprawdź czy kody kończą się na '2020'.
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
#
# code1: True
# code2: False

code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'

print(f'code1: {code1.endswith("2020")}')
print(f'code2: {code2.endswith("2020")}')

# ćwiczenie 4

# Dane są poniższe ścieżki:
#
# path1 = 'youtube.com/watch?v=5EhRztVxums'
# path2 = 'google.com/search?q=car'
# Używając odpowiedniej metody sprawdź czy podane ścieżki odnoszą się do
# serwisu YouTube (np. zaczynają się od 'youtube').
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
#
# path1: True
# path2: False

path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

print(f'path1: {path1.startswith("youtube")}')
print(f'path2: {path2.startswith("youtube")}')

# ćwiczenei 5

# Dane są poniższe ścieżki:
#
# path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
# path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
# path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'
# Używając odpowiedniej metody znajdź wyraz 'scientist'
# w podanych ścieżkach zwracając numer indeksu dla pierwszej litery odnalezionego wyrazu.
# Jeżeli wyrazu nie ma w ścieżce metoda zwróci wartość -1. Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
#
# path1: 49
# path2: 49
# path3: -1

path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'

print(f'path1: {path1.find("scientist")}')
print(f'path2: {path2.find("scientist")}')
print(f'path3: {path3.find("scientist")}')

# ćwiczenie 6

# Dane są poniższe kody:
#
# code1 = 'FVNISJND-20'
# code2 = 'FVNISJND20'
# Używając odpowiedniej metody sprawdź czy kody składają się tylko ze znaków alfanumerycznych (cyfry + litery)?
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
#
# code1: False
# code2: True

code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'

print(f'code1: {code1.isalnum()}')
print(f'code2: {code2.isalnum()}')

# ćwiczenie 7

# Dany jest poniższy tekst:
#
# text = 'Google Colab'
# Używając odpowiedniej metody zamień wszystkie duże litery na małe.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# google colab

text = 'Google Colab'
print(text.lower())

# ćwiczenie 8

# Dany jest poniższy tekst:
#
# text = 'Google Colab'
# Używając odpowiedniej metody zamień wszystkie litery na duże. W
# ynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# GOOGLE COLAB

text = 'Google Colab'
print(text.upper())

# ćwiczenie 9

# Dany jest poniższy tekst:
#
# text = '  Google Colab   '
# Używając odpowiedniej metody usuń białe znaki dookoła tekstu.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# Google Colab

text = '  Google Colab   '
print(text.strip())

# ćwiczenie 10

# Dany jest poniższy kod:
#
# code = 'FVNISJND-XX'
# Używając odpowiedniej metody zamień znak myślnika na spację.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# FVNISJND XX

code = 'FVNISJND-XX'
print(code.replace('-', ' '))

# ćwiczenie 11

# Dany jest poniższy tekst:
#
# text = '340-23-245-235'
# Używając odpowiedniej metody usuń wszystkie myślniki z tekstu.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# 34023245235

text = '340-23-245-235'
print(text.replace('-', ''))

# ćwiczenie 12

# Dany jest poniższy tekst:
#
# text = 'Open,High,Low,Close'
# Używając odpowiedniej metody podziel tekst według przecinka otrzymując listę.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# ['Open', 'High', 'Low', 'Close']

text = 'Open,High,Low,Close'
print(text.split(','))

# ćwiczenie 13

# Dany jest poniższy tekst:
#
# text = """Python jest językiem ogólnego przeznaczenia.
# Python jest popularny."""
# Używając odpowiedniej metody podziel tekst na zdania otrzymując listę.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# ['Python jest językiem ogólnego przeznaczenia.', 'Python jest popularny.']

text = """Python jest językiem ogólnego przeznaczenia.
Python jest popularny."""

print(text.splitlines())

# ćwiczenie 14

# Podana jest zmienna:
#
# num = 34
# Wykorzystując odpowiednią metodę dla obiektu typu str wydrukuj do konsoli
# zmienną num poprzedzoną czterema zerami.
# Oczekiwany wynik:
#
# 000034

num = 34
num = str(num)
print(num.zfill(6))

# Alternatywne rozwiązanie:

num = 34
print(str(num).zfill(6))

# ćwiczenie 15

# Z podanego adresu url:
#
# url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
# wytnij nazwę ścieżki po ostatnim znaku '/'.
# Następnie zamień wszystkie myślniki na spacje. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# sciezka data scientist machine learning engineer

url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
name = url.split('/')[-1]
name = name.replace('-', ' ')
print(name)

