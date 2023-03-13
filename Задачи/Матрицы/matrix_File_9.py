# # some_var = None
# some_var = (2,)
#
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# a = '' # пустая строка
# b = a or 1
#
# print(b)

# a = "foo"
# b = "bar"
#
# print(1 and a or b)

# a = ""
# b = "bar"
#
# print(1 and a or b)

# пусть a и b - переменные, которые мы хотим проверить
a = input("Введите значение: ")
b = input("Введите значение: ")
# if a and b: # проверка истинности обеих переменных
#         print("Обе переменные истинные")
#         print(a,b)

if a and b :
    print("Обе переменные истинные")
    print(a,b)
elif a or b:
    print("Одна из переменных истинная")
    print(a or b) # печать значения одной переменной, которая является истинной