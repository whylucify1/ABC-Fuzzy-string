
'''

In the code I provided, the -= operator is used to subtract the length of the first name from the randomly chosen index if the index falls outside the range of the first name.

For example, if the length of the first name is 5 and the randomly chosen index is 8 (i.e., greater than or equal to 5), then typo_index -= len(first_name) subtracts 5 from 8, resulting in typo_index being equal to 3. This value is then used as the index within the last name to insert the typo.

So, a -= b is just a shorthand way of writing a = a - b, which subtracts the value of b from the value of a and assigns the result back to a.

'''

#%%

uid = 'UID-289'
theme = 'Names where Name Parts are Modified'
category = 'Typos'
sub_category = '> 2 typos different name parts'
entity_type = 'individual'

#%%
import pandas as pd
#import numpy as np
#x = 5 # change when you want different results
#np.random.seed(x)
import random
import string

def insert_random_typos(name, n_typos):
    parts = name.split(', ')
    first_name = parts[1]
    last_name = parts[0]
    
    for i in range(n_typos):
        typo_index = random.randint(0, len(first_name) + len(last_name) - 1) # randomly choose a position within the name
        if typo_index < len(first_name):
            first_name = first_name[:typo_index] + random.choice(string.ascii_letters) + first_name[typo_index + 1:] # insert the typo in the first name
        else:
            typo_index -= len(first_name)
            last_name = last_name[:typo_index] + random.choice(string.ascii_letters) + last_name[typo_index + 1:] # insert the typo in the last name
    
    modified_name = last_name + ', ' + first_name
    return modified_name.upper()

#%%
ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')]
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)

#%%

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    final_test_name = insert_random_typos(row['name'], 3)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)

#%%

final_test_cases.to_csv('new csv files/289.csv', index=False)   