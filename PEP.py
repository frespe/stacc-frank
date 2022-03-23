import csv
from collections import Counter

def open_file():
    with open("pep_small.csv", "r", encoding="utf-8") as data_file:
        data = csv.DictReader(data_file)
        elements = list(data)
        return elements

data = open_file()
politicalParties = ['CIA World Leaders', 'CIA World Leaders;Every Politician', 'Every Politician;Members of the European Parliament', 'Members of the CoE Parliamentary Assembly;Members of the European Parliament', 'Every Politician', 'CIA World Leaders;Members of the CoE Parliamentary Assembly', 'Members of the CoE Parliamentary Assembly', 'CIA World Leaders;Members of the European Parliament', 'Every Politician;Members of the CoE Parliamentary Assembly;Members of the European Parliament', 'Members of the European Commitee of the Regions', 'Members of the European Parliament']



def pep_check(file, political):
    PEP = False
    for p in file:
        if p["dataset"] in political:
            PEP = True
    return PEP

def get_sanctions(files):
    sanctions = False
    if files["sanctions"] == "":
        sanctions = True

    return sanctions

def high_risk_countries():
    return None

def check_person_for_sanctions(datas):
    for persons in data:
        checkSanction = get_sanctions(persons)
        if checkSanction:
            print([f'{persons["name"]} Has not any sanctions'])
        else:
            print([f'{persons["name"]} has the following sanctions: {persons["sanctions"]}'])


check_person_for_sanctions(data)

def KYC():
    return None


# if __name__ == '__main__':
#     data = open_file()

#     pep = pep_check(data, politicalParties)
#     sanctions = get_sanctions(data)

#     halla = input("Please enter a name or organisation")
#     check_person_for_sanctions(data,halla)


