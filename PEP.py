import csv
from hashlib import new
import json
import pandas as pd
from collections import Counter

# #forklar why
# read_file = pd.read_excel ("iso_2digit_alpha_country_codes.xls")
# read_file.to_csv ("2digit.csv", index = None, header=True)
# df = pd.DataFrame(pd.read_csv("2digit.csv"))



def open_file():
    with open("pep_small.csv", "r", encoding="utf-8") as data_file:
        data = csv.DictReader(data_file)
        elements = list(data)
        return elements


data = open_file()


def pep_check(files):
    politicalParties = []
    PEP = False

    if files["dataset"] not in politicalParties:
        politicalParties.append(files["dataset"])
        PEP = True
    return PEP

def get_organisation():
    #List of high-risk countries
    hrc = ["Albania Barbados","Burkina Faso","Cambodia","Cayman Islands","Democratic People's Republic of Korea (DPRK)","Haiti","Iran","Jamaica","Jordan","Mali","Malta","Morocco","Myanmar","Nicaragua","Pakistan","Panama","Philippines","Senegal","South Sudan","Syria","Turkey","Uganda","Yemen","Zimbabwe"]
    newHrc = []
    with open("2digit.csv", "r", encoding="utf-8") as data_file:
        data = data_file.read()
        data = data.split("\n")

        countryCode = {}
        for i in data:
            i = i.split(',')
            if len(i)>1:
                key = i[0].lower()
                value = i[1]
                countryCode[key] = value
        for k,v in countryCode.items():
            for i in hrc:
                if i == v:
                    newHrc.append(k)
        return newHrc

def get_sanctions(files):
    sanctions = False
    if files["sanctions"] == "":
        sanctions = True

    return sanctions

def check_person_for_sanctions(data):
    inp = input("Enter name to check if there are any sanctions")
    for persons in data:
        if inp == persons["name"]:
            checkSanction = get_sanctions(persons)
            if checkSanction:
                print([f'{persons["name"]} Has not any sanctions'])
            else:
                print(
                    [f'{persons["name"]} has the following sanctions: {persons["sanctions"]}, please further investigate'])

#check_person_for_sanctions(data)

def check_person_for_PEP(data):
    inp = input("Enter name to check if PEP")
    for persons in data:
        if inp == persons["name"]:
            checkPEP = pep_check(persons)
            if not checkPEP:
                print([f'{persons["name"]} Is not a PEP'])
            else:
                print([f'{persons["name"]} is PEP: {persons["dataset"]}, please further investigate'])
#check_person_for_PEP(data)

def KYC():
    return None


# if __name__ == '__main__':
#     data = open_file()

#     pep = pep_check(data, politicalParties)
#     sanctions = get_sanctions(data)

#     halla = input("Please enter a name or organisation")
#     check_person_for_sanctions(data,halla)
