# ćwiczenie 1

# Napisz program,
# który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych przecinkiem.
# Wskazówka:
# Użyj pętli while oraz instrukcji break.
# Oczekiwany wynik:
#
# 2,3,5,7,11,13,17,19,23,29

# a = 1
#
# while True:
#     a = a + 1
#     i = 2
#     while i < a:
#         if a % i != 0:
#             if i == a-1:
#                 print(a)
#         else:
#             break
#         i = i + 1

# Alternatywne rozwiazanie:

counter = 0
number = 2
prime = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1

print(','.join(prime))

# ćwiczenie 2

# Wykorzystując pętlę while policz ile trzeba czekać lat,
# aby zwrot z poniżej opisanej inwestycji co najmniej się podwoił
# (pod uwagę bierzemy tylko pełne okresy).
# Oznaczenia:
# n - liczba okresów (w latach)
# pv - present value - wartość obecna
# r - stopa procentowa (roczna)
# fv - future value - wartość przyszła
# Opis inwestycji:
# pv = 1000
# r = 0.04
# Oczekiwany wynik:
# Wartość przyszła: 2025.82 PLN. Liczba okresów: 18 lat

# Oznaczenia:
# n - liczba okresów (w latach)
# pv - present value - wartość obecna
# r - stopa procentowa (roczna)
# fv - future value - wartość przyszła
# Opis inwestycji:
pv = 1000
r = 0.04
n = 0
fv = 0
while True:
    if fv > 2 * 1000:
        break
    else:
        pv = pv * (r + 1)
        n += 1
        fv = pv
        # print(pv)
print(pv)
print(n)

# Rozwiązanie alternatywne:

n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)

while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat')

# ćwiczenie 3

# Użyj algorytmu stochastycznego spadku wzdłuż gradientu do
# znalezienia minimum funkcji straty określonej wzorem:
#
# Pochodna tej funkcji to
#
#
#
# Przybliżona zasada działania algorytmu:
#
# 1. Zaczynamy od punktu startowego należącego do dziedziny funkcji, weźmy
#
# w_0 = -1
# 2. Określamy z góry maksymalną liczbę iteracji:
#
# max_iters = 10000
# 3. Określamy zmienną, która pomoże nam kontrolować rozmiar kroku w
# kierunku minimum, ustalmy jej wartość na 1
#
# previous_step_size = 1
# 4. Określamy wskaźnik uczenia:
#
# learning_rate = 0.01
# 5. Określamy precyzję jaka wystarczy do znalezienia minimum:
#
# precision = 0.000001
# 6. Definiujemy pochodną jako funkcję:
# derivative = lambda w: 2 * w - 4
# Aby znaleźć minimum funkcji L należy poruszać się wzdłuż kierunku
# przeciwnego do kierunku wyznaczanego przez gradient funkcji L
# aktualizując wartość w_0 następująco:
# w_0 = w_0 - learning_rate * derivative(w_prev)
# gdzie w_prev jest punktem z poprzedniej iteracji.
# Dla pierwszego korku jest to po prostu w_0.
# Zbuduj pętlę while, która pozwoli zatrzymać działanie algorytmu w momencie,
# gdy minimum zostanie odnalezione z zakładaną przez nas wartością precyzji lub
# przekroczymy maksymalną liczbę iteracji.
# Wskazówka: Warunki w pętli while:
# while previous_step_size > precision and iters < max_iters:
# Oczekiwany wynik:
# Minimum lokalne w punkcie: 2.00

max_iters = 10000
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_0 - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1

print(f'Minimum lokalne w punkcie: {w_0:.2f}')

# ćwiczenie 4

# Napisz program, który sprawdzi czy podany element (target)
# znajduje się w posortowanej liście (numbers). Podane są:
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 7
# Zasada działania algorytmu:
#
# 1. Ustalamy indeks startowy (start) oraz końcowy (end) oraz flagę flag = None.
#
# 2. Dopóki indeks startowy jest nie większy niż indeks końcowy wybieramy
# środkowy indeks (mid) listy (średnia arytmetyczna indeksu startowego i
# końcowego -> pamiętać o skonwertowaniu wyniku funkcją int). J
# eżeli indeks startowy jest większy niż indeks końcowy kończymy działanie algorytmu.
#
# 3. Sprawdzamy czy element listy dla tak obliczonego indeksu jest naszym szukanym
# (target). Jeżeli tak, ustawiamy flagę flag na wartość True i
# kończymy działanie algorytmu. Jeżeli nie -> krok 4.
#
# 4. Sprawdzamy, czy wartość elementu listy dla indeksu mid jest mniejsza niż target.
# Jeśli tak, to zwiększamy indeks startowy o 1. J
# eśli nie, zmniejszamy indeks końcowy o 1 i przechodzimy do kroku 2.
#
# Po wykonaniu pętli while w zależności od wartości flagi flag wydrukuj do
# konsoli tekst: 'Znaleziono', 'Nie znaleziono'.
# Oczekiwany wynik:
#
# Znaleziono

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
flag = None
start_index = 0
end_index = len(numbers) - 1
mid_index = 0
while start_index <= end_index:
    mid_index = int((start_index + end_index) / 2)
    if target == numbers[mid_index]:
        flag = True
        break
    else:
        if target > numbers[mid_index]:
            start_index += 1
        else:
            end_index -= 1
if flag is None:
    print('Nie znaleziono')
else:
    print('Znaleziono')

# Alternatywne rozwiązanie:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start + end) / 2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

if flag:
    print('Znaleziono')
else:
    print('Nie znaleziono')