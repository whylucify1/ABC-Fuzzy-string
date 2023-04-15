# ********************
# TEST CASE TYPE REFERENCE INFORMATION
# ********************

uid = 'UID-151'
theme = 'Name Part Variations'
category = 'Name Part Abbreviation'
sub_category = 'First and middle name abbreviation'
entity_type = 'Individual'

#%%
import numpy as np
x = 5  # change when you want different results
np.random.seed(x)

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

import pandas as pd

def abbreviate_first_and_middle_name(full_name):
    name_parts = full_name.split(', ')
    last_name = name_parts[0]
    
    if len(name_parts) > 1:
        first_middle_names = name_parts[1].split()
        
        if len(first_middle_names) > 1:
            first_name = first_middle_names[0]
            first_initial = first_name[0].upper()
            middle_name = first_middle_names[1]
            middle_initial = middle_name[:3].upper()
            first_middle_names[0] = first_initial
            first_middle_names[1] = middle_initial
            return f"{first_middle_names[0]} {first_middle_names[1]} {last_name.upper()}"
        else:
            return f"{first_middle_names[0]} {last_name.upper()}"
    else:
        return last_name.upper()

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0, 1, 2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')]  # only evaluate individuals
ofac_list_sampled = ofac_list_filtered.sample(n=500)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    final_test_name = abbreviate_first_and_middle_name(row['name'])
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

final_test_cases.to_csv('final_test_cases_151.csv', index=False, columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Original Name', 'Test Case Name'])
