import csv

from colorama import Fore


# Skriver om excel-fil til csv-fil
# read_file = pd.read_excel ("iso_2digit_alpha_country_codes.xls")
# read_file.to_csv ("2digit.csv", index = None, header=True)
# df = pd.DataFrame(pd.read_csv("2digit.csv"))


#Her bruker eg den minste csv-filen. Dette for å effektivt teste opp i mot metodene eg lager
def open_file():
    with open("pep_small.csv", "r", encoding="utf-8") as data_file:
        data = csv.DictReader(data_file)
        elements = list(data)
        return elements


data = open_file()

#Hjelpefunksjon for PEP-metoden lenger nede
def pep_check(persons):
    data = open_file()
    PEP = False
    politicalParties = []
    #Legger til alt av det som eg tolket som "politisk-engasjerte roller"
    for i in data:
        if i["dataset"] not in politicalParties:
            politicalParties.append(i)
    
    if persons["dataset"] in politicalParties or persons["dataset"]!="":
        PEP = True
    return PEP


#Metode for å hente ut landekoden for "high risk countries", 
#slik at eg kan sammenligne retur-verdien mot countries-kolonnen i csv-filen
def get_high_risk_country():
    # Liste av "high-risk countries"
    hrc = ["Albania Barbados", "Burkina Faso", "Cambodia", "Cayman Islands",
           "Democratic People's Republic of Korea (DPRK)", "Haiti", "Iran", "Jamaica", "Jordan", "Mali", "Malta", "Morocco", "Myanmar", "Nicaragua", "Pakistan", "Panama", "Philippines", "Senegal", "South Sudan", "Syria", "Turkey", "Uganda", "Yemen", "Zimbabwe"]
    newHrc = []
    with open("2digit.csv", "r", encoding="utf-8") as data_file:
        data = data_file.read()
        data = data.split("\n")


        countryCode = {}
        for i in data:
            i = i.split(',')
            if len(i) > 1:
                key = i[0].lower()
                value = i[1]
                countryCode[key] = value
        for key, value in countryCode.items():
            if value in hrc:
                newHrc.append(key)
        return newHrc

#Hjelpefunksjon for Sanksjon-metoden lenger nede
def get_sanctions(files):
    sanctions = False
    if files["sanctions"] == "":
        sanctions = True

    return sanctions

#Sanksjon-sjekk av person
def sanction_check(data):
    validInput = False
    while not validInput:
        inp = input("Enter name to check if there are any sanctions: ").lower()
        inp2 = input("Please enter the persons ID: ").lower()

        for persons in data:
            if inp == persons["name"].lower() and inp2 == persons["id"].lower():
                validInput = True
                checkSanction = get_sanctions(persons)
                if checkSanction:
                    print([f'{persons["name"]} Has no sanctions, continue to perfom a PEP-check'])
                else:
                    print(
                        [f'{persons["name"]} has the following sanctions: {persons["sanctions"]}, please further investigate'])
        if not validInput:
            print(Fore.RED + "That is not a valid name or ID for that person. Please try again " + Fore.RESET)
            
                       
            


#PEP sjekk for person
def PEP_check(data):
    validInput = False
    while not validInput:
        inp = input("Enter name to check if PEP: ").lower()
        inp2 = input("Please enter the persons ID: ").lower()
    
        for persons in data:
            if inp == persons["name"].lower() and inp2 == persons["id"].lower():
                validInput = True
                highRisk = get_high_risk_country()
                checkPEP = pep_check(persons)
                if not checkPEP:
                    print([f'{persons["name"]} Is not a PEP'])
                elif checkPEP and persons["countries"] in highRisk:
                    print([f'{persons["name"]} is a PEP: {persons["dataset"]}, and a part of a high risk country: {persons["countries"]}. please further investigate'])
                elif not checkPEP and persons["countries"] in highRisk:
                    print([f'{persons["name"]} is not a PEP, but is a part of a high risk country: {persons["countries"]}. please further investigate'])
                elif checkPEP:
                    print([f'{persons["name"]} is PEP: {persons["dataset"]}, please further investigate'])

        if not validInput:
            print(Fore.RED + "That is not a valid name or ID for that person. Please try again " + Fore.RESET)
            
def main():

    data = open_file()

    sanction_check(data)
    PEP_check(data)

if __name__ == '__main__':
    main()
