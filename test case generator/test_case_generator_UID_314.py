# *********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-314' 
theme = 'Names where name parts are modified'
category = 'typos'
sub_category = 'Typo niose name parts'
entity_type = 'Entity'

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

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

#%%

import random

def add_typo(name_part):
    # Choose a random index to modify
    typo_index = random.randint(0, len(name_part)-1)
    # Replace the character at the typo index with a random character
    typo_char = chr(random.randint(97, 122))
    modified_name_part = name_part[:typo_index] + typo_char + name_part[typo_index+1:]
    return modified_name_part

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
#run loop to generate the test cases 
import random

for index, row in ofac_list_sampled.iterrows():
   active_name = row['name']
   name_parts = active_name.split()

   # Split the full name into its name parts
   name_parts = active_name.split()

   # Choose the name part to modify
   name_part_to_modify = random.choice(name_parts)

   # Modify the name part by adding a typo
   name_part_with_typo = add_typo(name_part_to_modify)

   # Replace the modified name part in the original name
   name_parts[name_parts.index(name_part_to_modify)] = name_part_with_typo

   # Join the modified name parts back into a full name
   final_name = ' '.join(name_parts)
   
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)

