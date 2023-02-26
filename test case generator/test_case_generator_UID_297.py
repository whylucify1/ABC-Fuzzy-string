# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-297' 
theme = 'Names where name parts are modified'
category = 'typos'
sub_category = '>2 typos, same name part, no adjacent'
entity_type = 'individuals'

# ********************

#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_3
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)


#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
#run loop to generate the test cases 
import random

def add_typos(name_part):
    # Generate a list of non-adjacent random indices
    name_len = len(name_part)
    num_typos = 3
    typo_indices = sorted(random.sample(range(name_len), num_typos))
    while any(typo_indices[i+1] - typo_indices[i] == 1 for i in range(len(typo_indices)-1)):
        typo_indices = sorted(random.sample(range(name_len), num_typos))
    # Insert a random character at each typo index
    modified_name_part = name_part
    for i, typo_index in enumerate(typo_indices):
        typo_char = chr(random.randint(97, 122))
        modified_name_part = modified_name_part[:typo_index+i] + typo_char + modified_name_part[typo_index+i+1:]
    return modified_name_part


for index, row in ofac_list_sampled.iterrows():
   active_name = row['name']
   name_parts = active_name.split()

   # Choose the name part to modify
   name_part_to_modify = random.choice(name_parts)

   # Modify the name part by adding typos
   name_part_with_typos = add_typos(name_part_to_modify)

   # Replace the modified name part in the original name
   name_parts[name_parts.index(name_part_to_modify)] = name_part_with_typos

   # Join the modified name parts back into a full name
   final_name = ' '.join(name_parts)
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)
   
   

   