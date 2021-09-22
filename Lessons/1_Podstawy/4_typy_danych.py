
# ćwiczenie 1

# Dane są następujące zmienne (var1 - pusty string, var2 - spacja, var3 - znak nowej linii):
#
# var1 = ''
# var2 = ' '
# var3 = '\n'
# Wydrukuj do konsoli typ każdej zmiennej w osobnej linii.
#
# Oczekiwany wynik:
#
# <class 'str'>
# <class 'str'>
# <class 'str'>

var1 = ''
var2 = ' '
var3 = '\n'

print(type(var1))
print(type(var2))
print(type(var3))

# ćwiczenie 2

# var1 = None
# var2 = False
# var3 = 'True'
# Wydrukuj do konsoli typ każdej zmiennej w osobnej linii.
# Oczekiwany wynik:
#
# <class 'NoneType'>
# <class 'bool'>
# <class 'str'>

var1 = None
var2 = False
var3 = 'True'

print(type(var1))
print(type(var2))
print(type(var3))

# ćwiczenie 3

# Sprawdź, czy zmienna:
#
# flag = False
# jest instancją klasy bool. Wynik wydrukuj do konsoli.
# Wskazówka! Użyj funkcji isinstance()
# Oczekiwany wynik:
#
# True

flag = False
print(isinstance(flag, bool))

