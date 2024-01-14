import random

list_1 = []

n = 3
m = 3
h = 2
for i in range(0, n):
    temp = []
    for j in range(0, m):
        random_value = random.randint(0, 1)
        temp.append(random_value)
        print(random_value, end=' ')
    list_1.append(temp)
    print()
print()

for i in range(m):
    for j in range(n):
        if list_1[i][j] == 1:
            list_1[i][j] += 1
        print(list_1[i][j], end=' ')
    print()
