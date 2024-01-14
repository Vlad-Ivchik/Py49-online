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
