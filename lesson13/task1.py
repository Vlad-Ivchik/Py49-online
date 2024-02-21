def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


number = int(input("Введите определённое число в последовательности Фибоначчи: "))

list_fib = []
for num in fibonacci(number):
    list_fib.append(num)
print(list_fib)
