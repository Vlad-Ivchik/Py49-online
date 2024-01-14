n = int(input('Введите сколько стоит телефон: '))

k = int(input('Введите сумму, которую Маша может откладывать каждый день: '))

days = 0

money = 0

while money < n:
    days += 1
    if days % 7 != 0:
        money += k

print(f'Маша накопит нужную сумму за {days} дней')
