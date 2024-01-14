import random

list_1 = []

size = 15
for i in range(0, size):
    temp = []
    for j in range(0, size):
        random_value = random.randint(0, 101)
        temp.append(random_value)
        print(random_value, end=' ')
    list_1.append(temp)
    print()
print()
summ = 0
for i in range(0, size):
    for j in range(0, size):
        summ += list_1[i][j]

print(f"Сумма массива размером {size} х {size} равна {summ}\n")