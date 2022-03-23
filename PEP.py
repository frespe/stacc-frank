import csv
from collections import Counter

def open_file():
    with open("pep.csv", "r", encoding="utf-8") as data_file:
        data = csv.DictReader(data_file)
        elements = list(data)
        return elements

politicalParties = ['CIA World Leaders', 'CIA World Leaders;Every Politician', 'Every Politician;Members of the European Parliament', 'Members of the CoE Parliamentary Assembly;Members of the European Parliament', 'Every Politician', 'CIA World Leaders;Members of the CoE Parliamentary Assembly', 'Members of the CoE Parliamentary Assembly', 'CIA World Leaders;Members of the European Parliament', 'Every Politician;Members of the CoE Parliamentary Assembly;Members of the European Parliament', 'Members of the European Commitee of the Regions', 'Members of the European Parliament']

data = open_file()


def pep_check(file, political):
    PEP = False
    for person in file:
        if person["dataset"] in political:
            PEP = True
    return PEP


pep_check(data)

def get_sanctions(files):
    sanctions = False

    if files["sanctions"] == "":
        sanctions = True

    return sanctions



