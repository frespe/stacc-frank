import csv

with open("pep.csv", "r", encoding="utf-8") as data_file:
    data = csv.DictReader(data_file)

    for i in data:
        print(i)