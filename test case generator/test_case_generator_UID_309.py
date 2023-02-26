
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-309' 
theme = 'Names where name parts are modified'
category = 'typos'
sub_category = '2 typos- same part- adjacent'
entity_type = 'individual'

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

for index, row in ofac_list_sampled.iterrows():
   active_name = row['name']
   # Split the full name into its name parts
   name_parts = active_name.split()

   # Choose a random name part to modify
   name_part_index = random.randint(0, len(name_parts) - 1)
   name_part = name_parts[name_part_index]

   # Choose a random index to insert the first typo
   typo_index1 = random.randint(0, len(name_part) - 2)  # the -2 is to ensure that there is room for an adjacent typo

   # Choose a random character to insert as the first typo
   typo_char1 = chr(random.randint(97, 122))  # lowercase letter between a and z

   # Insert the first typo character at the first typo index
   name_part_with_typo1 = name_part[:typo_index1-1] + typo_char1 + name_part[typo_index1:]

   # Choose a random index to insert the second typo
   typo_index2 = typo_index1 + 1  # make the second typo adjacent to the first typo

   # Choose a random character to insert as the second typo
   typo_char2 = chr(random.randint(97, 122))  # lowercase letter between a and z

   # Insert the second typo character at the second typo index
   name_part_with_typos = name_part_with_typo1[:typo_index2-1] + typo_char2 + name_part_with_typo1[typo_index2:]

   # Replace the modified name part in the original name
   name_parts[name_part_index] = name_part_with_typos

   # Join the modified name parts back into a full name
   final_name = ' '.join(name_parts)
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)

    