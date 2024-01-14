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
