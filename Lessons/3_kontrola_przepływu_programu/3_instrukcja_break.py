
# ćwiczenie 1

# Napisz program, który porówna dwie listy i zwróci wartość True w przypadku
# gdy listy będą zawierały co najmniej jeden ten sam element.
# W przeciwnym razie zwróci wartość False.
# Wynik wydrukuj do konsoli.
# Podane listy:
# list1 = [1, 2, 0]
# list2 = [4, 5, 6, 1]
# Oczekiwany wynik:
# True

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

for number in list1:
    if number in list2:
        print('True')
        break
    else:
        print('False')
        break

# Alternatywne rozwiązanie:

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False

for item1 in list1:
    if item1 in list2:
        result = True
        break

print(result)

# ćwiczenie 2

# Podana jest lista hashtagów:
# hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
# Sprawdź, czy każdy obiekt z listy jest obiektem klasy str.
# Jeżeli tak wydrukuj wartość True, w przeciwnym przypadku wydrukuj wartość False.
# Oczekiwany wynik:
# False

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True

for name in hashtags:
    if name is not str(name):
        result = False
        break
print(result)

# Alternatywne rozwiązanie:

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True

for hashtag in hashtags:
    if not isinstance(hashtag, str):
        result = False
        break

print(result)
