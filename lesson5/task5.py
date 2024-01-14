list_1 = list(input('Введите список чисел через пробел ').split())
print(list_1)

set_list = set(list_1)

for item in set_list:
    count = list_1.count(item)
    if count > 1:
        print(f"Элемент {item} встречается {count} раз")
