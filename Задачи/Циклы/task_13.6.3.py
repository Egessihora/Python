# TASK 13.6.3
# Напишите программу, которая будет печатать лесенку следующего типа:
#
# n = 3
# *
# **
# ***
#
# n = 4
# *
# **
# ***
# ****
# Число n может быть любым.

n = int(input("Введите количество звёздочек: "))

for i in range(0, n):
    print('*' * (i+1))
