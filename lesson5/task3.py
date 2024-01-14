n = int(input('Введите длинну ряда Фибоначчи: '))
a = 1
b = 1

for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
