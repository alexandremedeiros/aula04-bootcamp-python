# Leitura de Arquivos csv ####################################################

import csv

path = "exemplo.csv"

data = []

with open(path, mode="r", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    
    for row in dict_reader:
        data.append(row)

for row in data:
    print(row)

print()