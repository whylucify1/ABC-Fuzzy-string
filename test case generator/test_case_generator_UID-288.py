uid = 'UID-288' 
theme = 'Names where name parts are modified'
category = 'Typos'
sub_category = '> 2 Typos different name parts'
entity_type = 'Entity'

#%%

import pandas as pd
#import numpy as np
#x = 5 # change when you want different results
#np.random.seed(x)
import random
import string

def insert_random_typos(name, n_typos):
    for i in range(n_typos):
        typo_index = random.randint(0, len(name) - 1) # choose a random index within the entire name
        while name[typo_index].isspace():  # make sure the selected character is not a space
            typo_index = random.randint(0, len(name) - 1)
        typo_letter = random.choice(string.ascii_letters)
        name = name[:typo_index] + typo_letter + name[typo_index + 1:]
    
    return name.upper()

#%%

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')]
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)

#%%

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    final_test_name = insert_random_typos(row['name'], 3)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)

#%%

final_test_cases.to_csv('new csv files/288.csv', index=False)   