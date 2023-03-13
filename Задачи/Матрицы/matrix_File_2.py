random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берем каждую строку
   min_index = 0  # в качестве минимального значения возьмем первый элемент строки
   max_index = 0
   min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
   max_value = row[max_index]  # для максимального значения тоже самое

# Так как таблица представляет собой список списков, первый цикл будет принимать целую строку.
# Мы не знаем значение минимального элемента, поэтому возьмем первый элемент в качестве минимального
# и будем искать элемент меньше него. Аналогично поступим с максимальным элементом.
   for index_col in range(len(row)):
       if row[index_col] < min_value:
           min_value = row[index_col]
           min_index = index_col
       if row[index_col] > max_value:
           max_value = row[index_col]
           max_index = index_col
   min_value_rows.append(min_value)
   min_index_rows.append(min_index)
   max_value_rows.append(max_value)
   max_index_rows.append(max_index)

print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)


