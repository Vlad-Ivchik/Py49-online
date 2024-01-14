'''Тема: Работа с текстом, сериализация и файловая система'''

'''1.Работа с модулем os
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
• Вывести имя вашей ОС
• Вывести путь до папки, в которой вы находитесь
• Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются все
файлы с расширением .txt, то же самое для остальных
расширений
• После рассортировки выводится сообщение типа «в папке с
текстовыми файлами перемещено 5 файлов, их суммарный
размер – 50 гигабайт»
• Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод сообщения
типа «Файл data.txt был переименован в some_data.txt»
• Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами.'''

import os
import platform

name_os = platform.system()
print(f'Имя операционной системы: {name_os}')

main_path = os.getcwd()
print(f'Текущая директория где находитесь: {main_path}')

for i in range(1, 4):
    if not os.path.exists(str(i) + '.txt'):
        text_file = open(str(i) + '.txt', "w")
        text_file.close()

    if not os.path.exists(str(i) + '.json'):
        text_file = open(str(i) + '.json', "w")
        text_file.close()

sum_txt = 0
count_files = 0
count_files_json = 0

for i in os.listdir():
    if os.path.splitext(i)[1] == '.txt':
        count_files += 1
        sum_txt += os.stat(i).st_size
        if not os.path.exists("texts"):
            os.mkdir('texts')
        os.replace(i, 'texts/' + i)

print(f'В папку с текстовыми файлами перемещено {count_files} файлов, их суммарный размер – {sum_txt} байт')

sum_json = 0
for i in os.listdir():
    if os.path.splitext(i)[1] == '.json':
        count_files_json += 1
        sum_json += os.stat(i).st_size
        if not os.path.exists("jsons"):
            os.mkdir('jsons')
        os.replace(i, 'jsons/' + i)

print(f'В папку с json файлами перемещено {count_files_json} файлов, их суммарный размер – {sum_json} байт')

os.chdir('texts')
for i in os.listdir():
    os.rename(i, 'hello' + i)
    y = 'hello' + i
    print(f'Файл {i} был переименован в {y}')
os.chdir(main_path)

'''2. Замена имён в судебном решении
Написать программу, которая заменит в тексте ФИО подсудимого
на N. Каждое слово в ФИО начинается с заглавной буквы, фамилия
может быть двойная.
Пример.
Вводимый текст:
Подсудимая Эверт-Колокольцева Елизавета Александровна
в судебном заседании вину инкриминируемого правонарушения
признала в полном объёме и суду показала, что 14 сентября
1876 года, будучи в состоянии алкогольного опьянения
от безысходности, в связи с состоянием здоровья позвонила
со своего стационарного телефона в полицию, сообщив о том, что
у неё в квартире якобы заложена бомба. После чего приехали
TeachMeSkills.by
сотрудники полиции, скорая и пожарные, которым она сообщила,
что бомба — это она.
Вывод:
«Подсудимая N в судебном заседании» и далее по тексту'''

import re

text = ('Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину инкриминируемого\n'
        'правонарушения признала в полном объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии\n'
        'алкогольного опьянения от безысходности, в связи с состоянием здоровья позвонила со своего стационарного\n'
        'телефона в полицию, сообщив о том, что у неё в квартире якобы заложена бомба. После чего приехали\n'
        'сотрудники полиции, скорая и пожарные, которым она сообщила, что бомба — это она.')

print(re.sub(r'[А-ЯЁ]\w*'
             r'(?:-[А-ЯЁ]\w*)?'
             r'(?: [А-ЯЁ]\w*){2}', 'N', text))

'''3. Напишите программу, которая считывает текст из файла (в
файле может быть больше одной строки) и выводит в новый
файл самое часто встречаемое слово в каждой строке и число
– счётчик количества повторений этого слова в строке.'''

# string = 'Привет как дела, привет отлично, привет отлично'
with open("123.txt") as string:
    string = string.read()


def finder(string):
    words = string.lower().split()
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    print(max(counter.values()))

    return max(counter, key=counter.get)


print(finder(string))

'''4. Напишите программу, которая получает на вход строку с
названием текстового файла и выводит на экран содержимое
этого файла, заменяя все запрещённые слова звездочками.
Запрещённые слова, разделённые символом пробела, должны
храниться в файле stop_words.txt.
Программа должна находить запрещённые слова в любом месте
файла, даже в середине другого слова. Замена независима от
регистра: если в списке запрещённых есть слово exam, то
замениться должны exam, eXam, EXAm и другие вариации.
Пример.
в stop_words.txt записаны слова: hello email python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python IS the
programming language of thE future. My EMAIL is... PYTHON as
AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming language of
*** future. My ***** **... ****** ** awesome!!!!'''

import re

with open('text2.txt') as e, open('words.txt') as d:
    text, exceptions = e.read(), d.read().split()
for i in exceptions:
    text = re.sub(i, '*' * len(i), text, flags=re.I)
print(text)

'''5. В текстовый файл построчно записаны фамилия и имя
учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов.'''

with open("class.txt") as file:
    summary = 0
    counter = 0
    for i in file:
        i = i.split()
        y = int(i[2])
        summary += y
        counter += 1
        if y < 3:
            print(*i)


'''6. В файл записано некоторое содержимое (буквы, цифры,
пробелы, специальные символы и т.д.). Числом назовём
последовательность цифр, идущих подряд. Вывести сумму
всех чисел, записанных в файле.
Пример.
Входные данные: 123 ааа456 1x2y3z 4 5 6
Выходные данные: 600'''


with open("primer.txt") as s:
    s = s.read()

    length = len(s)
    integers = []
    i = 0  # индекс текущего символа

    while i < length:
        s_int = ''  # строка для нового числа
        while i < length and '0' <= s[i] <= '9':
            s_int += s[i]
            i += 1
        i += 1
        if s_int != '':
            integers.append(int(s_int))

    print(sum(integers))



'''7. Дан текстовый файл с несколькими строками. Зашифровать
шифром Цезаря, при этом шаг зависит от номера строки: для
первой строки шаг 1, для второй – 2 и т.д.
Пример.
Входные данные:
Hello
Hello
Hello
Hello
Выходные данные:
Ifmmp
Jgnnq
Khoor
Lipps'''


def ceasar_encode(letter, shift):
    result = ''
    for letter in line:
        if letter.isalpha():
            number = ord(letter) + shift % 32
            if number > 1103:
                number -= 32
            result += chr(number)
        else:
            result += letter
    return result


with open("ceasar.txt") as text:
    text = text.read().split()
for shift, line in enumerate(text, 1):
    print(ceasar_encode(line, shift))


''''8. JSON и CSV.
Исходные данные:
https://drive.google.com/drive/folders/1KH3pJewo3QKl3mua2XnJDv9xN
2LxusbE?usp=sharing
Пункты задания:
• Есть данные в формате JSON – взять с диска с исходными
данными.
• Реализовать функцию, которая считает данные из исходного
JSON-файла и преобразует их в формат CSV
• Реализовать функцию, которая сохранит данные в CSV-файл
(данные должны сохраняться независимо от их количества –
если добавить в исходный JSON-файл ещё одного
сотрудника, работа программы не должна нарушаться).
• Реализовать функцию, которая добавит информацию о новом
сотруднике в JSON-файл. Пошагово вводятся все
необходимые данные о сотруднике, формируются данные для
записи.
• Такая же функция для добавления информации о новом
сотруднике в CSV-файл.
• Реализовать функцию, которая выведет информацию об
одном сотруднике по имени. Имя для поиска вводится с
клавиатуры.
• Реализовать функцию фильтра по языку: с клавиатуры
вводится язык программирования, выводится список всех
сотрудников, кто владеет этим языком программирования.
• Реализовать функцию фильтра по году: ввести с клавиатуры
год рождения, вывести средний рост всех сотрудников, у
которых год рождения меньше заданного.
• Программа должна представлять собой интерактив –
пользовательское меню с возможностью выбора
определённого действия (действия – функции из предыдущих
пунктов + выход из программы). Пока пользователь не
выберет выход из программы, должен предлагаться выбор
следующего действия'''


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
