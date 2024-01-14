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
