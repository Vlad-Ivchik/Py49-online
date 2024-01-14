import csv
import json

with open("employees.json", 'r') as file:
    data = json.load(file)


with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('sw_data_new.csv') as f:
    print(f.read())