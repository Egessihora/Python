# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Значениями здесь являются целые числа (см. пример ниже).
# Необходимо на их основе создать словарь d с помощью функции dict()
# и вывести его на экран командой: print(*sorted(d.items()))
#
# Sample Input:
# one=1 two=2 three=3
#
# Sample Output:
# ('one', 1) ('three', 3) ('two', 2)

lst = input("Ввести пары ключ=значение через пробел: ").split()
lst_2 = []

for el in lst:
    lst_2.append(el.split('='))

for el in range(len(lst_2)):
    lst_2[el][1] = int(lst_2[el][1])

d = dict(lst_2)
print(*sorted(d.items()))
