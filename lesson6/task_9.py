import random

list_1 = []

n = 3
m = 3
for i in range(0, n):
    temp = []
    for j in range(0, m):
        random_value = random.randint(0, 101)
        temp.append(random_value)
        print(random_value, end=' ')
    list_1.append(temp)
    print()
print()
summ_1 = 0
summ = 0
for i in range(0, n):
    for j in range(0, m):
        summ += list_1[i][j]

sum_column = [0, 0, 0]

for i in list_1:

    sum_column[0] += i[0]

    sum_column[1] += i[1]

    sum_column[2] += i[2]

print(sum_column)

print(f"Сумма массива размером {n} х {m} равна {summ}\n")

percent = (sum_column[0] / summ) * 100
print(f'Сумма элементов первого столбца = {sum_column[0]}')
print(f'Сумма элементов первого столбца в процентах составляет: ~ {percent:.0f} %')


percent_2 = (sum_column[1] / summ) * 100
print(f'Сумма элементов второго столбца = {sum_column[1]}')
print(f'Сумма элементов второго столбца в процентах составляет: ~ {percent_2:.0f} %')

percent_3 = (sum_column[2] / summ) * 100
print(f'Сумма элементов третьего столбца = {sum_column[2]}')
print(f'Сумма элементов третьего столбца в процентах составляет: ~ {percent_3:.0f} %')
