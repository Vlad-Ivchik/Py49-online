from random import randint

size = 10000

container = [randint(0, 100) for i in range(size)]


def pow(list_1: list[int]) -> list[int]:
    list_2 =[]
    for i in list_1:
        i = i**2
        list_2.append(i)

    print(list_1)
