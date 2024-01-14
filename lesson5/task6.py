# list_1 = [1, 3, 5, 7, 9, 11, 13, 15]
list_1 = list(input('Введите список чисел через пробел ').split())
n = input('Введите искомый элемент из списка ')
start = 0
end = len(list_1) - 1
while start <= end:
    mid = (start + end) // 2
    if list_1[mid] == n:
        print(f'Позиция искомого элемента в исходном списке равна {mid}')
    if list_1[mid] > n:
        end = mid - 1
    else:
        start = mid + 1
