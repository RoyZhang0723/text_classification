import csv
import os
import pandas as pd

# refine data
dfs = []
files = os.walk(r"NLP_data")
for path, dir_list, file_list in files:
    for file_name in file_list:
        print(os.path.join(path, file_name))
        dfs.append(pd.read_csv(os.path.join(path, file_name), delimiter="\t"))
contractorAB1 = dfs[0]['ID']
mediaAB = dfs[1]['ID']
greenGroupAB = dfs[2]['ID']
governmentAB = dfs[3]['ID']
subContractorAB = dfs[4]['ID']
politicalPartyAb = dfs[5]['ID']
NGOAB = dfs[6]['ID']
workerAB = dfs[7]['ID']
consultantAB = dfs[8]['ID']
surveyorAB = dfs[9]['ID']
environmentalGroupAB = dfs[10]['ID']
communityAB = dfs[11]['ID']
residentAB = dfs[12]['ID']
designerAB = dfs[13]['ID']
contractorAB2 = dfs[14]['ID']
contractorAB = pd.concat([contractorAB1, contractorAB2], axis=0)

print("1 media:", len(mediaAB))
print("2 green group:", len(greenGroupAB))
print("3 government:", len(governmentAB))
print("4 subcontractor:", len(subContractorAB))
print("5 political party:", len(politicalPartyAb))
print("6 NGO", len(NGOAB))
print("7 worker", len(workerAB))
print("8 consultant", len(consultantAB))
print("9 surveyor", len(surveyorAB))
print("10 environmental group", len(environmentalGroupAB))
print("11 community", len(communityAB))
print("12 resident", len(residentAB))
print("13 designer", len(designerAB))
print("14 contractor", len(contractorAB))

rows = []
# media:1 , green group:2 , government:3 , subcontractor:4 , political party:5 , NGO:6
# worker:7 , consultant:8 , surveyor:9 , environmental group:10 , community:11 , resident:12
# designer:13 , contractor:14
dict = {}
for i in mediaAB:
    dict['label'] = 1
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in greenGroupAB:
    dict['label'] = 2
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in governmentAB:
    dict['label'] = 3
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in subContractorAB:
    dict['label'] = 4
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in politicalPartyAb:
    dict['label'] = 5
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in NGOAB:
    dict['label'] = 6
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in workerAB:
    dict['label'] = 7
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in consultantAB:
    dict['label'] = 8
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in surveyorAB:
    dict['label'] = 9
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in environmentalGroupAB:
    dict['label'] = 10
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in communityAB:
    dict['label'] = 11
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in residentAB:
    dict['label'] = 12
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in designerAB:
    dict['label'] = 13
    dict['abstract'] = i
    rows.append(dict)
    dict = {}

for i in contractorAB:
    dict['label'] = 14
    dict['abstract'] = i
    rows.append(dict)
    dict = {}


with open(r'data.csv', 'w', newline='') as csvFile:
    headers = ['label', 'abstract']
    fileWriter = csv.DictWriter(csvFile, headers)
    fileWriter.writeheader()
    fileWriter.writerows(rows)

