# TASK 13.6.2

# Посчитайте произведение всех чисел от 1 до N включительно
# P =   # заводим переменную-счетчик, в которой мы будем считать произведение,
# подумайте чему она должна быть равна.
# N = 5
# Запишите цикл for для подсчета произведения.

P = 1
N = int(input("Введите натуральное число: "))

for i in range(1, N + 1):
    P *= i
print("Ответ: произведение всех чисел равно = ", P)