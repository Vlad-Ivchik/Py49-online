import random

list_1 = []

n = 3
m = 3
h = 2
for i in range(0, n):
    temp = []
    for j in range(0, m):
        random_value = random.randint(0, 10)
        temp.append(random_value)
        print(random_value, end=' ')
    list_1.append(temp)
    print()

for i in range(m):
    for j in range(n):
        if list_1[j][i] == h:
            print(f'Столбец {i + 1} имеет цифру {h}')