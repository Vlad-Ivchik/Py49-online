import csv
import json

with open("employees.json", 'r') as file:
    data = json.load(file)

csv_columns1 = []

for i in data:
    for key in i.keys():
        if key in csv_columns1:
            continue
        else:
            csv_columns1.append(key)

print(csv_columns1)

with open('data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns1)
    writer.writeheader()
    for i in data:
        writer.writerow(i)

data1 = {
    "name": str(input('Введи имя ')),
    "birthday": str(input('Введи др ')),
    "height": int(input('Введи рост ')),
    "weight": float(input('Введи вес ')),
    "car": False,
    "languages": list(input('Введи языки ').split(', '))
}

with open('employees.json', 'r') as file:
    data3 = json.load(file)
    print(data3)
    data3.append(data1)

with open('employees.json', 'w', encoding='utf8') as outfile:
    json.dump(data3, outfile, ensure_ascii=False, indent=2)

x = str(input('Для получения информации о сотруднике напишите как его зовут: '))

for i in data:
    for key, value in i.items():
        if value == x:
            print(i)


lang = input('Введите язык программирования: ')
for i in data:
    for z in i['languages']:
        if z == lang:
            print(i['name'])
