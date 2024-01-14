'''Тема: Функциональное программирование

1. Дан список чисел. С помощью map() получить список,
где каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
'''


numbers = [1, 2, 3]
print(numbers)
print(list(map(lambda x: f'‘{x}’', numbers)))

numbers = [1, 2, 3]
print(numbers)
print(list(map(str, numbers)))


'''2. Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых больше
0.'''


def even(x: int):
    if x > 0:
        return True
    return False


numbers = [-1, 0, 1, 2, 3]


print(list(filter(even, numbers)))

print(list(filter(lambda x: x > 0, numbers)))



'''3. Дан список строк. С помощью filter() получить список
тех строк из исходного списка, которые являются
палиндромами (читаются в обе стороны одинаково, например,
’abcсba’)'''


str_list = ["abccba", "123", "dadadad", "lol", "321123"]


def is_palindrome(word):
    return word.lower() == word[::-1].lower()


print(list(filter(is_palindrome, str_list)))

print(list(filter(lambda x: x.lower() == x[::-1].lower(), str_list)))



'''4. Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.'''


import random
import time


def measure_time(function):
    def inner(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end = time.time()
        print(f"Функция отработала за:{(end - start_time):.2f} секунд")

    return inner


size = 10000000

container = [random.randint(0, 100) for x in range(size)]


@measure_time
def lamdba_pow(list_1: list[int]) -> list[int]:
    return list(map(lambda x: x ** 2, list_1))


@measure_time
def pow(list_1: list[int]) -> list[int]:
    list_2 = []
    for i in list_1:
        list_2.append(i ** 2)
    return list_2


pow(container)
lamdba_pow(container)



'''5. Используя map() и reduce() посчитать площадь
квартиры, имея на входе характеристики комнат квартиры.
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]'''


from functools import reduce


def square(x):
    return x["length"] * x["width"]


def summary(a, b):
    return a + b


rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

print(reduce(summary, list(map(square, rooms))))
