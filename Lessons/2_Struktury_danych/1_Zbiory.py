
# ćwiczenie 1

# Dany jest zbiór:
#
# przedmioty = {'matematyka', 'polski'}
# Używając odpowiedniej metody dodaj kolejny przedmiot 'angielski'
# do zbioru przedmioty. Zbiór wydrukuj do konsoli.
# Oczekiwany wynik:
#
# {'angielski', 'matematyka', 'polski'}
# Uwaga:
# Pamiętaj, że zbiór to nieuporządkowana struktura danych. Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

przedmioty = {'matematyka', 'polski'}
przedmioty.add('angielski')
print(przedmioty)

# ćwiczenie 2

# Dany jest tekst:
#
# text = 'Programming in python.'
# Wykonaj kolejne kroki:
#
# Zamień wszystkie litery na małe.
# Usuń spacje i kropkę.
# Utwórz zbiór składający się z wszystkich liter w tak otrzymanym tekście.
# Odpowiednią metodą dla zbiorów usuń z tego zbioru wszystkie samogłoski
# (zbiór vowels):
# vowels = {'a', 'e', 'i', 'o', 'u'}
#  5. Wydrukuj liczbę elementów w tak przetworzonym zbiorze
#  (inaczej liczba samogłosek) tak jak pokazano poniżej.
# Oczekiwany wynik:
#
# Liczba elementów: x

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
text_1 = set(text.lower().replace(' ', '').replace('.', ''))
consonants = text_1.difference(vowels)
print(consonants)
print(f'Liczba elementów: {len(consonants)}')

# Alternatywne rozwiązanie:

text = 'Programming in python.'
text = text.lower()
text = text.replace(' ', '')
text = text.replace('.', '')
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set(text)
consonants = letters.difference(vowels)
print(consonants)
print(f'Liczba elementów: {len(consonants)}')

# ćwiczenie 3

# Różnica symetryczna dwóch zbiorów to zbiór składający się
# z wszystkich elementów tych zbiorów oprócz elementów wspólnych.
#
# Niech podane będą zbiory:
#
# A = {2, 4, 6, 8}
# B = {4, 10}
# Używając właściwej metody wyznacz różnicę symetryczną zbiorów A i B.
# Wynik wydrukuj do konsoli.
# Oczekiwany wynik:
# Różnica symetryczna: {2, 6, 8, 10}
# Uwaga:
#
# Pamiętaj, że zbiór to nieuporządkowana struktura danych.
# Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

A = {2, 4, 6, 8}
B = {4, 10}
C = A.symmetric_difference(B)
print('Różnica symetryczna:', C)

# Alternatywne rozwiązanie:

A = {2, 4, 6, 8}
B = {4, 10}
sym_diff = A.symmetric_difference(B)
print(f'Różnica symetryczna: {sym_diff}')

# ćwiczenie 4

# Mamy podane dwa zbiory ID klientów,
# którzy skorzystali (dokonali zakupu) odpowiednio z reklamy pierwszej
# (ad1_id) oraz drugiej (ad2_id):
#
# ad1_id = {'001', '002', '003'}
# ad2_id = {'002', '003', '007'}
# W kampanii reklamowej można skorzystać z 2 ofert reklamowych.
# Wybierz ID klientów, do których można wysłać kolejną reklamę
# (inaczej id, które pojawiły się tylko raz).
# Oczekiwany wynik:
# Wybrane ID: {'007', '001'}
# Uwaga:
#
# Pamiętaj, że zbiór to nieuporządkowana struktura danych.
# Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
ad3_id = ad1_id.symmetric_difference(ad2_id)
print(f'Wybrane ID: {ad3_id}')

# ćwiczenei 5

# Podane są dwa zbiory ID klientów.
# Pierwszy mówi o tym czy dana osoba kliknęła w baner reklamowy.
# Drugi, czy dana osoba zakupiła produkt.
#
# is_clicked = {'9001', '9002', '9005'}
# is_bought = {'9002', '9004', '9005'}
# Zwróć ID tych klientów, którzy kliknęli w reklamę i kupili produkt.
# Oczekiwany wynik:
# ID klientów: {'9002', '9005'}
# Uwaga:
# Pamiętaj, że zbiór to nieuporządkowana struktura danych.
# Możesz otrzymać inną kolejność elementów niż w oczekiwanym wyniku.

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
is_all = is_bought.intersection(is_clicked)
print(f'ID klientów: {is_all}')
