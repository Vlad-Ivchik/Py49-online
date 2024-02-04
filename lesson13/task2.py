def cycle(*args, n):
    i = 0
    while i < n:
        yield args[i % len(args)]
        i += 1


numbers_list = input("Введите числа циклической последовательности через пробел: ").split()
n = int(input("Введите количество чисел которые необходимо вывести: "))

cyclic = cycle(*numbers_list, n=n)

list_numbers = []
for number in cyclic:
    list_numbers.append(number)
print(list_numbers)
