'''Тема: Структурное программирование
1. Дан список чисел, отсортированных по возрастанию. На
вход принимается значение, равное одному из элементов
списка. Реализовать функцию, выполняющую рекурсивный
алгоритм бинарного поиска, на выходе программа должна
вывести позицию искомого элемента в исходном списке.'''


def binarySearch(list_input, start, end, x):
    # Check base case
    if end >= start:

        mid = start + (end - start) // 2

        # If element is present at the middle itself
        if list_input[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif list_input[mid] > x:
            return binarySearch(list_input, start, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(list_input, mid + 1, end, x)

    # Element is not present in the array
    else:
        return -1


# Driver Code
if __name__ == '__main__':
    list_1 = [2, 3, 4, 10, 40]
    n = 11

    # Function call
    result = binarySearch(list_1, 0, len(list_1) - 1, n)

    if result != -1:
        print("Позиция искомого элемента в исходном списке", result)
    else:
        print("Искомый элемент не найден в списке")


'''2. Программа получает на вход число в десятичной
системе счисления. Реализовать функцию, которая переводит
входное число в двоичную систему счисления. Допускается
реализация функции как в рекурсивном варианте, так и с
итеративным подходом.'''

def function(x, y):
    while x > 0:
        z = x % 2
        y = str(z) + y
        x = x // 2

    print(y)


function(27, '')


'''3. Программа получает на вход число. Реализовать
функцию, которая определяет, является ли это число простым
(делится только на единицу и на само себя)'''

def simple_number(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


print(simple_number(3))


'''4. Программа получает на вход два числа и находит их
НОД (наибольший общий делитель). Пример: на вход подаются
числа 12 и 18, их НОД равен 6'''

def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


print(get_nod(10, 15))


'''5. Программа получает на вход строку – сообщение и
указание, что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное
сообщение шифром Цезаря, вторая – расшифровывает. В
зависимости от выбора пользователя (шифровать или
дешифровать) вызывается соответствующая функция,
результат выводится в консоль'''

alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение для ДЕшифровки: ").upper()
itog = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
else:
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
print(itog)


'''7. Реализовать функцию, которая создаёт матрицу
размером M строк на N столбцов и заполняет её рандомными
числами.'''

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


'''8. Реализовать функцию, которая находит минимальный и
максимальный элементы в матрице (матрица M x N). Вывести в
консоль индексы найденных элементов'''


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

'''9. Реализовать функцию, которая находит сумму
элементов матрицы (матрица M x N). Определить, какую долю
в общей сумме (процент) составляет сумма элементов каждого
столбца'''


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


'''12. Программа получает на вход число H. Реализовать
функцию, которая определяет, какие столбцы имеют хотя бы
одно такое же число, а какие не имеют (матрица M x N)'''


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


'''13. Реализовать функцию, которая находит сумму
элементов на главной диагонали и сумму элементов на
побочной диагонали (матрица M x N)'''


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


'''14. Дана матрица M x N. Исходная матрица состоит из
нулей и единиц. Реализовать функцию, которая добавит к
матрице ещё один столбец, элементы которого делает
количество единиц в соответствующей строке чётным'''


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
