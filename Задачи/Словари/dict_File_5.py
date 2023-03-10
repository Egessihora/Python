# На вход программы поступают данные в виде набора строк в формате:
# ключ1=значение1
# ключ2=значение2
# ...
# ключN=значениеN
#
# Ключами здесь выступают целые числа (см. пример ниже).
# Необходимо их преобразовать в словарь d (без использования функции dict())
# и вывести его на экран командой: print(*sorted(d.items()))
#
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
#
# Sample Input:
# 5=отлично
# 4=хорошо
# 3=удовлетворительно
#
# Sample Output:
# (3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')

pairs = input("Ввести пару ключ=значение: ")
lst = []

while pairs !='':
    if pairs not in lst:
        lst.append(pairs)
    pairs = input("Ввести пару ключ=значение: ")

lst_2 = []
for el in lst:
    lst_2.append(el.split())

for el in range(len(lst_2)):
    lst_2[el] = lst[el].split('=')

d = {}

for el in range(len(lst_2)):
    d[int(lst_2[el][0])] = lst_2[el][1]

(*sorted(d.items()))
