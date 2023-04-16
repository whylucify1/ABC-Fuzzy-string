uid = 'UID-292' 
theme = 'Names where name parts are modified'
category = 'Typos'
sub_category = '> 2 Typos same name part - Adjacent, at beginning'
entity_type = 'Entity'

#%%

import pandas as pd
#import numpy as np
#x = 5 # change when you want different results
#np.random.seed(x)
import random
import string

def insert_adjacent_typos_at_beginning(name, n_typos):
    words = name.split(' ')
    first_word = words[0]
    
    for _ in range(n_typos):
        typo_index = random.randint(0, 1)
        typo_letter = random.choice(string.ascii_letters)
        first_word = first_word[:typo_index] + typo_letter + random.choice(string.ascii_letters) + first_word[typo_index + 2:]
    
    modified_name = first_word + ' ' + ' '.join(words[1:])
    return modified_name.upper()

#%%

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')]
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

#%%

for index, row in ofac_list_sampled.iterrows():
    modified_name = insert_adjacent_typos_at_beginning(row['name'], 2)
    final_test_name = modified_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)

#%%

final_test_cases.to_csv('new csv files/292.csv', index=False)   