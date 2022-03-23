import csv
from collections import Counter

def open_file():
    with open("pep_small.csv", "r", encoding="utf-8") as data_file:
        data = csv.DictReader(data_file)
        elements = list(data)
        return elements

data = open_file()



def pep_check(files):
    politicalParties = ['CIA World Leaders', 'CIA World Leaders;Every Politician', 'Every Politician;Members of the European Parliament', 'Members of the CoE Parliamentary Assembly;Members of the European Parliament', 'Every Politician', 'CIA World Leaders;Members of the CoE Parliamentary Assembly', 'Members of the CoE Parliamentary Assembly', 'CIA World Leaders;Members of the European Parliament', 'Every Politician;Members of the CoE Parliamentary Assembly;Members of the European Parliament', 'Members of the European Commitee of the Regions', 'Members of the European Parliament']
  
    PEP = False
    for i in politicalParties:
        if files["dataset"] in i:
            PEP = True
    return PEP


def get_sanctions(files):
    sanctions = False
    if files["sanctions"] == "":
        sanctions = True

    return sanctions

def high_risk_countries():
    return None

def check_person_for_sanctions(data):
    inp = input("Enter name to check the sanction")
    for persons in data:
        if inp == persons["name"]:
            checkSanction = get_sanctions(persons)
            if checkSanction:
                print([f'{persons["name"]} Has not any sanctions'])
            else:
                print([f'{persons["name"]} has the following sanctions: {persons["sanctions"]}'])
#check_person_for_sanctions(data)

def check_person_for_PEP(data):
    #inp = input("Enter name to check if PEP")
    for persons in data:
        #if inp == persons["name"]:
        checkPEP = pep_check(persons)
        if not checkPEP:
            print([f'{persons["name"]} Is not a PEP'])
        else:
            print([f'{persons["name"]} is: {persons["dataset"]}'])
check_person_for_PEP(data)


def KYC():
    return None


# if __name__ == '__main__':
#     data = open_file()

#     pep = pep_check(data, politicalParties)
#     sanctions = get_sanctions(data)

#     halla = input("Please enter a name or organisation")
#     check_person_for_sanctions(data,halla)


