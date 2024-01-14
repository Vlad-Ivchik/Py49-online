import math

# 1
a = int(input('Введите значение "a"'))
b = int(input('Введите значение "b"'))
x = int(input('Введите значение "x"'))

y = (a**2 / 3) + (a**2 + 4 / b) + (math.sqrt(a**2 + 4) / 4) + (math.sqrt(a**2 + 4)**3 / 4)

print(f'Результат по заданию "a" = {y}')

# 2
y = math.cos(x) + math.sin(x)

print(f'Результат по заданию "b" = {y}')

# 3
y = pow(math.cos(x**2)**2 + math.sin(2*x - 1)**2, 1/3)

print(f'Результат по заданию "c" = {y}')

# 4
y = 5*x + 3*x**2 * math.sqrt(1 + math.sin(x)**2)

print(f'Результат по заданию "d" = {y}')
