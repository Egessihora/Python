# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
def rec_sum(n):
   if n == 1:  # терминальный случай
       return 1
   return n + rec_sum(n - 1)  # рекурсивный вызов

n = rec_sum(6)
print(n)


# С помощью рекурсивной функции разверните строку.
def reverse_str(string):
   if len(string) == 0:
       return ''
   else:
       return string[-1] + reverse_str(string[:-1])

t = reverse_str('test')  # tset
print(t)