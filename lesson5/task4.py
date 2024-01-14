numbers = list(input('Введите список чисел через пробел').split())

total = 0

for num in numbers:
    total += int(num)
numbers.sort()

print(numbers)
print(f'Минимальное число = {numbers[0]}')
print(f'Максимальное число = {numbers[-1]}')
print(f"Сумма чисел в списке: = {total}")
