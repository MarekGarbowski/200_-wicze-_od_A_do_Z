
# ćwiczenie 1

# Do podanej listy:
#
# cities = ['Warszawa', 'Łódź', 'Kraków']
# dodaj miasto 'Gdańsk'. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# ['Warszawa', 'Łódź', 'Kraków', 'Gdańsk']

cities = ['Warszawa', 'Łódź', 'Kraków']
cities += ['Gdańsk']
print(cities)

# Alternatywne rozwiązanie:

cities = ['Warszawa', 'Łódź', 'Kraków']
cities.append('Gdańsk')
print(cities)

# ćwiczenie 2

# Podana jest lista:
# idx = ['001', '002', '001', '003', '001']
# Używając odpowiedniej metody zlicz wystąpienia elementu '001'.
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
#
# Liczba wystąpień: 3

idx = ['001', '002', '001', '003', '001']
print(f'Liczba wystąpień: {idx.count("001")}')

# ćwiczenie 3

# Podany jest tekst:
#
# text = 'Programowanie w języku Python'
# Dokonaj standaryzacji tekstu (zamień duże litery na małe,
# zastąp polskie znaki w następujący sposób: 'ę' -> 'e').
# Następnie utwórz listę składającą się z unikalnych znaków w tekście.
# Usuń spację z tej listy oraz posortuj od a do z.
# Wydrukuj do konsoli 10 pierwszych elementów tej listy.
# Wskazówka:
# Do wygenerowania unikalnych znaków w tekście można użyć zbioru.
# Oczekiwany wynik:
#
# ['a', 'e', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o']

text = 'Programowanie w języku Python'
text = text.lower()
text = text.replace('ę', 'e').replace(' ', '')
text = sorted(text)
text = set(text)
text.update()
text = sorted(text)
# text.sort()
print(text[:10])

# Alternatywne rozwiązanie:

text = 'Programowanie w języku Python'
text = text.lower()
text = text.replace('ę', 'e')
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters[:10])

# ćwiczenie 4

# Podana jest lista:
# filenames = ['view.jpg', 'bear.jpg', 'ball.png']
# Dodaj do tej listy nazwę pliku 'phone.jpg' na początku listy.
# Następnie usuń nazwę pliku 'ball.png'.
# Tak otrzymaną listę wydrukuj do konsoli.
# Oczekiwany wynik:
# ['phone.jpg', 'view.jpg', 'bear.jpg']

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames = ['phone.jpg'] + filenames
filenames.remove('ball.png')
print(filenames)

# Alternatywne rozwiązanie:

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)

# ćwiczenie 5

# Podana jest lista id zamówień z danego dnia:
# day1 = ['3984', '9042', '4829', '2380']
# Używając odpowiedniej metody rozszerz tę listę o następny dzień:
# day2 = ['4231', '5234', '1345', '2455']
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# ['3984', '9042', '4829', '2380', '4231', '5234', '1345', '2455']

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day3 = day1 + day2
print(day3)

# Alternatywne rozwiązanie:

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)

# ćwiczenie 6

# Podany jest obiekt typu tuple:
#
# techs = ('python', 'java', 'sql', 'aws')
# Posortuj ten obiekt od a do z. Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# ('aws', 'java', 'python', 'sql')

techs = ('python', 'java', 'sql', 'aws')
print(tuple(sorted(techs)))

# ćwiczenie 7

# Podana jest lista:
#
# hashtags = ['summer', 'time', 'vibes']
# Używając odpowiedniej metody połącz elementy listy znakiem '#'.
# Dodaj także ten znak na początku otrzymanego tekstu.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
#
# #summer#time#vibes

hashtags = ['summer', 'time', 'vibes']
hashtags = '#'.join(hashtags)
print('#' + hashtags)

# Rozwiązanie alternatywne:

hashtags = ['summer', 'time', 'vibes']
print('#' + '#'.join(hashtags))

