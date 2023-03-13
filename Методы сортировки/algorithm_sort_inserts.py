# Алгоритм сортировки вставками

a = [-3, 5, 0, -8, 1, 10]
N = len(a)      # число элементов в списке

for i in range(1, N):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

print(a)
