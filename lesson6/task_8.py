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
min_number = list_1[0][0]
max_number = 0
for i in range(n):
    for j in range(m):
        if list_1[i][j] < min_number:
            min_number = list_1[i][j]
        elif list_1[i][j] > max_number:
            max_number = list_1[i][j]
print(f'Максимальное число в матрице = {max_number}, минимальное число в матрице = {min_number}')