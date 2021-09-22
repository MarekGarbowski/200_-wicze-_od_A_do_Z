
# ćwiczenie 1

# Napisz program, który wczyta plik playway.txt
# zawierający dane dotyczące notowań giełdowych spółki
# Playway i następnie policzy średnią cenę zamknięcia (3-dniowa średnia).
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
#
# 3-dniowa średnia cena zamknięcia: xxx.xx
with open('playway.txt', 'r') as file:
    line = file.read().splitlines()
    print(line)
close = []
for idx, line in enumerate(line):
    if idx > 0:
        close.append(int(line.split(',')[-2]))
        print(close)
close_avg = sum(close) / len(close)
print(close_avg)


# ćwiczenie 2

# Wczytaj plik indeksy.txt. W każdej linii jest inna nazwa indeksu publikowanego
# przez Giełdę Papierów Wartościowych w Warszawie.
# Utwórz listę z nazwami indeksów rozpoczynających się od 'WIG'.
# Wynik wydrukuj do konsoli.
#
# Pomocniczy wynik:
#
# ['WIG',
#  'WIG-banki',
#  'WIG-budownictwo',
#  'WIG-CEE',
#  'WIG-chemia',
#  'WIG-energia',
#  'WIG-ESG',
#  'WIG-górnictwo',
#  'WIG-informatyka',
#  'WIG-leki',
#  'WIG-media',
#  'WIG-motoryzacja',
#  'WIG-nieruchomości',
#  'WIG-odzież',
#  'WIG-paliwa',
#  'WIG-Poland',
#  'WIG-spożywczy',
#  'WIG-telekomunikacja',
#  'WIG-Ukraine',
#  'WIG.GAMES',
#  'WIG.MS-BAS',
#  'WIG.MS-FIN',
#  'WIG.MS-PET',
#  'WIG20',
#  'WIG20dvp',
#  'WIG20lev',
#  'WIG20short',
#  'WIG20TR',
#  'WIG30',
#  'WIG30TR',
#  'WIGdiv',
#  'WIGtech']
# Oczekiwany wynik:
#
# ['WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE', 'WIG-chemia',
# 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo', 'WIG-informatyka', 'WIG-leki',
# 'WIG-media', 'WIG-motoryzacja', 'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa',
# 'WIG-Poland', 'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine', 'WIG.GAMES',
# 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET', 'WIG20', 'WIG20dvp', 'WIG20lev',
# 'WIG20short', 'WIG20TR', 'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech']

with open('indeksy.txt', 'r') as file:
    line = file.read().splitlines()
wig = []
for name in line:
    if name.startswith('WIG'):
        wig.append(name)
print(wig)

# rozwiązanie alternatywne:

with open('indeksy.txt', 'r') as file:
    lines = file.read().splitlines()

indexes = [index for index in lines if index.startswith('WIG')]
print(indexes)
# ćwiczenie 3

# Podany jest plik plw_d.csv zawierający notowania spółki Playway za marzec 2020.
#
# Plik wczytano w następujący sposób:
#
# with open('plw_d.csv', 'r') as file:
#     content = file.read().splitlines()
# Zmienna content:
#
# ['Data,Otwarcie,Najwyzszy,Najnizszy,Zamkniecie,Wolumen',
#  '2020-03-02,305,324.5,283.5,310,64081',
#  '2020-03-03,325.5,340.5,320,340.5,55496',
#  '2020-03-04,324,340.5,315,330,36152',
#  '2020-03-05,344,344,310,315,35992',
#  '2020-03-06,306.5,307,291,305,32539',
#  '2020-03-09,274,291,250,258,79402',
#  '2020-03-10,278,284.5,256,264,35700',
#  '2020-03-11,270,270,238.5,245,60445',
#  '2020-03-12,218,228,196,197,94031',
#  '2020-03-13,210,229,198.8,211,100412',
#  '2020-03-16,205,248,197.8,240.5,50659',
#  '2020-03-17,245,269,232.5,264,99480',
#  '2020-03-18,264,280,251,270,70136',
#  '2020-03-19,267,280,267,279.5,30732',
#  '2020-03-20,297.5,307,280,280.5,43426',
#  '2020-03-23,274,289,258,285,37098',
#  '2020-03-24,305,309,296.5,309,31939',
#  '2020-03-25,313,330,295,304,46724',
#  '2020-03-26,300,309,295.5,300,27213',
#  '2020-03-27,302,306.5,290,296,13466',
#  '2020-03-30,299,300,287,300,10316',
#  '2020-03-31,302.5,309,302,306.5,15698']
# Przekształć zawartość pliku w taki sposób,
# aby otrzymać słownik zawierający dwa klucze:
# 'Data', 'Zamkniecie'. Wartościami dla tych kluczy będą odpowiednio
# listy składające się z dat oraz cen zamknięcia.
# Cenę zamknięcia skonwertuj na typ float. Wynik wydrukuj do konsoli.
#
#
#
# Pomocniczy wynik:
#
# {'Data': ['2020-03-02',
#   '2020-03-03',
#   '2020-03-04',
#   '2020-03-05',
#   '2020-03-06',
#   '2020-03-09',
#   '2020-03-10',
#   '2020-03-11',
#   '2020-03-12',
#   '2020-03-13',
#   '2020-03-16',
#   '2020-03-17',
#   '2020-03-18',
#   '2020-03-19',
#   '2020-03-20',
#   '2020-03-23',
#   '2020-03-24',
#   '2020-03-25',
#   '2020-03-26',
#   '2020-03-27',
#   '2020-03-30',
#   '2020-03-31'],
#  'Zamkniecie': [310.0,
#   340.5,
#   330.0,
#   315.0,
#   305.0,
#   258.0,
#   264.0,
#   245.0,
#   197.0,
#   211.0,
#   240.5,
#   264.0,
#   270.0,
#   279.5,
#   280.5,
#   285.0,
#   309.0,
#   304.0,
#   300.0,
#   296.0,
#   300.0,
#   306.5]}
# Oczekiwany wynik:
#
# {'Data': ['2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05',
# '2020-03-06', '2020-03-09', '2020-03-10', '2020-03-11', '2020-03-12',
# '2020-03-13', '2020-03-16', '2020-03-17', '2020-03-18', '2020-03-19',
# '2020-03-20', '2020-03-23', '2020-03-24', '2020-03-25', '2020-03-26',
# '2020-03-27', '2020-03-30', '2020-03-31'],
# 'Zamkniecie': [310.0, 340.5, 330.0, 315.0, 305.0, 258.0, 264.0, 245.0, 197.0,
# 211.0, 240.5, 264.0, 270.0, 279.5, 280.5, 285.0, 309.0, 304.0, 300.0, 296.0,
# 300.0, 306.5]}

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[4]) for line in content]
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
    }
print(result)

# ćwiczenie 4

# Podany jest plik plw_d.csv zawierający notowania spółki Playway za marzec 2020.
#
# Plik wczytano w następujący sposób:
#
# with open('plw_d.csv', 'r') as file:
#     content = file.read().splitlines()
# Zmienna content:
#
# ['Data,Otwarcie,Najwyzszy,Najnizszy,Zamkniecie,Wolumen',
#  '2020-03-02,305,324.5,283.5,310,64081',
#  '2020-03-03,325.5,340.5,320,340.5,55496',
#  '2020-03-04,324,340.5,315,330,36152',
#  '2020-03-05,344,344,310,315,35992',
#  '2020-03-06,306.5,307,291,305,32539',
#  '2020-03-09,274,291,250,258,79402',
#  '2020-03-10,278,284.5,256,264,35700',
#  '2020-03-11,270,270,238.5,245,60445',
#  '2020-03-12,218,228,196,197,94031',
#  '2020-03-13,210,229,198.8,211,100412',
#  '2020-03-16,205,248,197.8,240.5,50659',
#  '2020-03-17,245,269,232.5,264,99480',
#  '2020-03-18,264,280,251,270,70136',
#  '2020-03-19,267,280,267,279.5,30732',
#  '2020-03-20,297.5,307,280,280.5,43426',
#  '2020-03-23,274,289,258,285,37098',
#  '2020-03-24,305,309,296.5,309,31939',
#  '2020-03-25,313,330,295,304,46724',
#  '2020-03-26,300,309,295.5,300,27213',
#  '2020-03-27,302,306.5,290,296,13466',
#  '2020-03-30,299,300,287,300,10316',
#  '2020-03-31,302.5,309,302,306.5,15698']
# Znajdź największą wartość wolumenu w podanym miesiącu.
# Wynik wydrukuj do konsoli.
#
# Oczekiwany wynik:
#
# Max Vol: 100412

# with open('plw_d.csv', 'r') as file:
#     content = file.read().splitlines()
#
# data = [(line.split(',')[0], line.split(',')[5]) for line in content]
# result = {
#     data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
#     data[0][1]: max([int(data[1:][i][1]) for i in range(len(data) - 1)])
#     }
# print(f'Max Vol: {max(result.values())}')

# Rozwiązanie alternatywne:

# with open('plw_d.csv', 'r') as file:
#     content = file.read().splitlines()
#
# volumes = [line.split(',')[-1] for line in content][1:]
# volumes = [int(vol) for vol in volumes]
# max_vol = max(volumes)
# print(f'Max Vol: {max_vol}')

# ćwiczenie 5

# Podany jest plik plw_d.csv zawierający notowania spółki Playway za marzec 2020.
#
# Plik wczytano w następujący sposób:
#
# with open('plw_d.csv', 'r') as file:
#     content = file.read().splitlines()
# Zmienna content:
#
# ['Data,Otwarcie,Najwyzszy,Najnizszy,Zamkniecie,Wolumen',
#  '2020-03-02,305,324.5,283.5,310,64081',
#  '2020-03-03,325.5,340.5,320,340.5,55496',
#  '2020-03-04,324,340.5,315,330,36152',
#  '2020-03-05,344,344,310,315,35992',
#  '2020-03-06,306.5,307,291,305,32539',
#  '2020-03-09,274,291,250,258,79402',
#  '2020-03-10,278,284.5,256,264,35700',
#  '2020-03-11,270,270,238.5,245,60445',
#  '2020-03-12,218,228,196,197,94031',
#  '2020-03-13,210,229,198.8,211,100412',
#  '2020-03-16,205,248,197.8,240.5,50659',
#  '2020-03-17,245,269,232.5,264,99480',
#  '2020-03-18,264,280,251,270,70136',
#  '2020-03-19,267,280,267,279.5,30732',
#  '2020-03-20,297.5,307,280,280.5,43426',
#  '2020-03-23,274,289,258,285,37098',
#  '2020-03-24,305,309,296.5,309,31939',
#  '2020-03-25,313,330,295,304,46724',
#  '2020-03-26,300,309,295.5,300,27213',
#  '2020-03-27,302,306.5,290,296,13466',
#  '2020-03-30,299,300,287,300,10316',
#  '2020-03-31,302.5,309,302,306.5,15698']
# Znajdź dzień z największą wartością wolumenu w podanym miesiącu.
# Wynik wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
# Data: 2020-03-13

with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[-1]) for line in content][1:]
data = [(val[0], int(val[1])) for val in data]
max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(f'Data: {max_date}')
