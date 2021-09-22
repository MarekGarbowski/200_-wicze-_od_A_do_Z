
# ćwiczenie 1

# Napisz program, który obliczy pole koła o promieniu 5 cm.
# Przyjmij w przybliżeniu wartość liczby pi:
# pi = 3.14
# Oczekiwany wynik:
# Pole koła wynosi: xx.x cm2

wheel_radius = 5
pi = 3.14
wheel_area = pi * (wheel_radius ** 2)
print(f'Pole koła wynosi: {wheel_area:.1f} cm2')

# ćwiczenie 2

# Napisz program, który wyznaczy wartość przyszłą kwoty 1000 PLN przy rocznej stopie procentowej 3%,
# kapitalizacji rocznej oraz 5-letnim okresie inwestycji. Wynik zaokrąglij do pełnych groszy.
# Oczekiwany wynik:
# Wartość końcowa inwestycji wynosi: xxxx.xx PLN

percentage = 1.03
years = 5
start_amount = 1000
investment = start_amount * percentage ** years

print(f'Wartość końcowa inwestycji wynosi: {investment:.2f} PLN')

# ćwiczenie 3

# Napisz program, który policzy deltę dla równania kwadratowego:
# 3x2 + 4x + 1 = 0
# Oczekiwany wynik:
#
# Delta wynosi: x

a = 3
b = -4
c = 1
delta = b ** 2 + 4 * a * c
print(f'Delta wynosi: {delta}')

# ćwiczenie 4

# Dany jest ciąg arytmetyczny:
#
# Oblicz sumę 10-ciu początkowych wyrazów tego ciągu.
# an = 10 + 4n
#
# Oczekiwany wynik:
# Suma pierwszych 10 wyrazów ciągu wynosi: xxx.x

max_range = 11
an = 0
for n in range(1, max_range):
    xx = 10 + 4 * n
    an += xx
    # print(an)
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {an:.1f}')

# Rozwiązanie alternatywne:
# a1 = 14
# a10 = 50
# n = 10
# s10 = ((a1 + a10) / 2) * n
# print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {s10}')

# ćwiczenie 5

# Dany jest ciąg geometryczny:
# an = 8 * 2**(n-1)
# Oblicz sumę 6-ciu pierwszych elementów tego ciągu.
# Oczekiwany wynik:
#
# Suma pierwszych 6 wyrazów ciągu wynosi: xxx.x

an_1 = 0
for n_1 in range(1, 7):
    x_1 = 8 * 2 ** (n_1 - 1)
    an_1 += x_1
    # print(an_1)
print(f'Suma pierwszych 6 wyrazów ciągu wynosi: {an_1:.1f}')

# Alternatywne rozwiązanie:
a1 = 8
a2 = 8 * 2
n = 6
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q))
print(f'Suma pierwszych {n} wyrazów ciągu wynosi: {s6}')

# ćwiczenie 6

# Dane jest równanie kwadratowe:
# x**2 + 5*x + 4 = 0
# Korzystając z wzorów Viete'a oblicz sumę oraz iloczyn pierwiastków
# będących rozwiązaniem równania. Wynik wydrukuj do konsoli taki jak
# pokazano poniżej.
#
# Oczekiwany wynik:
#
# x1+x2 = x.x
# x1x2 = x.x

a3 = 1
b3 = 5
c3 = 4
suma = -b3 / a3
iloczyn = c3 / a3
print(f'x1+x2 = {suma}\nx1x2 = {iloczyn}')

# ćwiczenie 7

# Wyznacz środek odcinka o końcach w punktach: A = (2, 4), B = (-4, 6).
#
# Oczekiwany wynik:
#
# Środek odcinka AB: (-1.0, 5.0)

a4 = (2, 4)
b4 = (-4, 6)
sum1 = ((a4[0] + b4[0]) / 2, (a4[1] + b4[1]) / 2)
print(f'Środek odcinka AB: {sum1}')

# Alternatywne rozwiązanie:
a1 = 2
a2 = 4
b1 = -4
b2 = 6
s1 = (a1 + b1) / 2
s2 = (a2 + b2) / 2
print(f'Środek odcinka AB: ({s1}, {s2})')

# ćwiczenie 8

# Oblicz odległość dwóch punktów A=(3, 2), B=(-1, -1).
#
# Oczekiwany wynik:
# Odległość punktów A i B wynosi: x.x

a5 = (3, 2)
b5 = (-1, -1)
distance = ((b5[0] - a5[0]) ** 2 + (b5[1] - a5[1]) ** 2) ** 0.5
print(f'Odległość punktów A i B wynosi: {distance}')

# Alternatywne rozwiązanie:
a6 = 3
a7 = 2
b6 = -1
b7 = -1
distance1 = ((b6 - a6) ** 2 + (b7 - a7) ** 2)**(1/2)
print(f'Odległość punktów A i B wynosi: {distance1}')

# ćwiczenie 9

# Znajdź pierwiastki równania kwadratowego:
# x**2 + 5*x + 4 = 0
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
#
# Oczekiwany wynik:
#
# x1 = x.x
# x2 = x.x

a = 1
b = 5
c = 4
delta = b ** 2 - 4 * a * c
delta_sqrt = delta ** (1/2)
x1 = (-b - delta_sqrt) / (2 * a)
x2 = (-b + delta_sqrt) / (2 * a)
print(f'x1 = {x1}')
print(f'x2 = {x2}')

# ćwiczenie 10

# Oblicz średnią geometryczną następujących liczb: 4, 3, 4.5, 5.
#
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.

# Oczekiwany wynik:
#
# Średnia geometryczna podanych liczb: x.xx

number_set = (4, 3, 4.5, 5)
number_set_mul = 1
for number in number_set:
    number_set_mul = number * number_set_mul
geometric_mean = number_set_mul ** (1 / len(number_set))
print(f'Średnia geometryczna podanych liczbL {geometric_mean:.2f}')

# Alternatywne rozwiązanie:

# x1, x2, x3, x4 = 4, 3, 4.5, 5
# geo = (x1 * x2 * x3 * x4)**(1/4)
# print(f'Średnia geometryczna podanych liczb: {geo:.2f}')

# ćwiczenei 11

# Dany jest nieskończony ciąg geometryczny:
# 1, 0.5, 0.25, 0.125, ....
# Oblicz sumę tego ciągu. Wynik wydrukuj do konsoli tak jak pokazano poniżej.
#
# Oczekiwany wynik:
#
# Suma ciągu wynosi: x.x

geometric_sequence = 1
start_sequence = 0.5
while start_sequence > 0:
    geometric_sequence += start_sequence
    start_sequence = start_sequence / 2
print(f'Suma ciągu wynosi: {geometric_sequence}')

# Alternatywne rozwiązanie:

a11 = 1
a22 = 1/2
q11 = a22 / a11
S11 = a11 / (1 - q11)
print(f'Suma ciągu wynosi: {S11}')

# ćwiczenie 12

# Oblicz odchylenie standardowe następującego zestawu danych: 10, 11, 9.
#
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
#
# Oczekiwany wynik:
#
# Odchylenie standardowe zestawu danych wynosi: x.xx

digit_set = [10, 11, 9]
mean = 0
standard_deviation = 0
for digit in digit_set:
    mean += digit
mean = mean / len(digit_set)
for digit_1 in digit_set:
    observation = (digit_1 - mean) ** 2
    standard_deviation += observation
standard_deviation = (standard_deviation / len(digit_set)) ** 0.5
print(f'Odchylenie standardowe zestawudanych wynosi: {standard_deviation:.2f}')

# Alternatywne rozwiązanie:

x1, x2, x3 = 10, 11, 9
mean = (x1 + x2 + x3) / 3.0
var = ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3.0
std = var**(1/2)
print(f'Odchylenie standardowe zestawu danych wynosi: {std:.2f}')
