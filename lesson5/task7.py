list_1 = [5, 6, 7, 1, 2, 3, 4]
n = 7
start = 0
end = len(list_1) - 1
while start <= end:
    mid = (start + end) // 2
    if list_1[mid] == n:
        print(f'Позиция искомого элемента в исходном списке равна {mid}')
    if list_1[mid] > n:
        end = mid - 1
    else:
        if n <= list_1[end]:
            start = mid + 1
        else:
            end = mid - 1
