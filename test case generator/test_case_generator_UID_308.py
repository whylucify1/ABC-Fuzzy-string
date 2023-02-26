
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-308' 
theme = 'Names where name parts are modified'
category = 'typos'
sub_category = 'two typos-same part-no adjacent'
entity_type = 'entity'

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

   # Choose a random name part to modify
   name_part_index = random.randint(0, len(name_parts) - 1)
   name_part = name_parts[name_part_index]

   # Choose two random indices to insert typos
   typo_index1 = random.randint(0, len(name_part) - 2)  # the -2 is to ensure that there is room for a non-adjacent typo
   typo_index2 = random.randint(typo_index1 + 2, len(name_part))  # the +2 ensures that the two typos are not adjacent

   # Choose a random character to insert at each typo index
   typo_char1 = chr(random.randint(97, 122))  # lowercase letter between a and z
   typo_char2 = chr(random.randint(97, 122))  # lowercase letter between a and z
   # Insert the typo characters at the typo indices
   name_part_with_typos = name_part[:typo_index1-1] + typo_char1 + name_part[typo_index1+1:typo_index2] + typo_char2 + name_part[typo_index2:]

   # Replace the modified name part in the original name
   name_parts[name_part_index] = name_part_with_typos

   # Join the modified name parts back into a full name
   final_name = ' '.join(name_parts)
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)



    