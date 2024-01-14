string = input("Введите слово")

count_h = string.count('h') - 1
print(string.replace('h', 'h').replace('h', 'H', count_h).replace('H', 'h', 1))
