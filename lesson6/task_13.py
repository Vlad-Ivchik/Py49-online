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

main = 0
not_main = 0

for i in range(n):
    main += list_1[i][i]
    not_main += list_1[i][n - i - 1]

print(main)
print(not_main)
