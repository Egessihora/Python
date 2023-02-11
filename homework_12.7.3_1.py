per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))

deposit = []

for key in per_cent.values():
           deposit.append(int(key*money/100))

print(deposit)

max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))
