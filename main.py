from transformers import BertTokenizer, BertModel, BertForMaskedLM
import csv
import pandas as pd
import os

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





