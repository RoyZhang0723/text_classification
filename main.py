from transformers import BertTokenizer, BertModel, BertForMaskedLM
import csv
import pandas as pd
import os
dfs = []
files = os.walk(r"NLP_data")
for path, dir_list, file_list in files:
    for file_name in file_list:
        print(os.path.join(path, file_name))
        dfs.append(pd.read_csv(os.path.join(path, file_name), delimiter="\t"))
contractorAB1 = dfs[0]['AB']
mediaAB = dfs[1]['AB']
greenGroupAB = dfs[2]['AB']
governmentAB = dfs[3]['AB']
subContractorAB = dfs[4]['AB']
politicalPartyAb = dfs[5]['AB']
NGOAB = dfs[6]['AB']
workerAB = dfs[7]['AB']
consultantAB = dfs[8]['AB']
surveyorAB = dfs[9]['AB']
environmentalGroupAB = dfs[10]['AB']
communityAB = dfs[11]['AB']
residentAB = dfs[12]['AB']
designerAB = dfs[13]['AB']
contractorAB2 = dfs[14]['AB']
contractorAB = pd.concat([contractorAB1, contractorAB2], axis=0)
print(contractorAB)

# csvFile = 'NLP_data/Community.csv'
# df = pd.read_csv(csvFile, delimiter="\t")
# print(df['AB'])
