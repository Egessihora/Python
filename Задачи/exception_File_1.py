# ОТЛОВ ОШИБОК (ИСКЛЮЧЕНИЙ)
#
# Создайте скрипт, который будет в input() принимать строки,
# их необходимо будет конвертировать в числа, добавьте try-except,
# чтобы строки могли быть сконвертированы в числа.
#
# В случае удачного выполнения скрипта пусть выведется: «Вы ввели правильное число».
#
# В конце скрипта обязательно должна быть надпись «Выход из программы».
#
# ПРИМЕЧАНИЕ: Для отлова ошибок используйте try-except, а также блоки finally и else.

# Пример входных данных: 1, -3, razdvatri (должно выдать ошибку)

try:
    print("Введите число: ")
    num = int(input())
except ValueError as e:
    print("Вы ввели неправильное число")
else:
    print("Вы ввели число " + str(num))
finally:
    print("Выход из программы")
