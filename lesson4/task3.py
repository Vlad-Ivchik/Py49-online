import math

R_1 = int(input('Введите радиус первой планеты'))
V_1 = int(input('Введите орбитальную скорость первой планеты'))
R_2 = int(input('Введите радиус второй планеты'))
V_2 = int(input('Введите орбитальную скорость второй планеты'))

L_1 = 2 * R_1 * math.pi / V_1
L_2 = 2 * R_2 * math.pi / V_2

print(f'Длинна года на первой планете {L_1}')
print(f'Длинна года на второй планете {L_2}')

if L_1 > L_2:
    print('Длинна года первой планеты больше второй')
elif L_1 == L_2:
    print('Длинна года первой планеты равно второй')
else:
    print('Длинна года первой планеты меньше второй')
