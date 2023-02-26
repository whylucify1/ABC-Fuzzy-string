# *********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-328' 
theme = 'Special Characters and Spaces'
category = 'Addition'
sub_category = '2 special character added'
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

import random

def add_special_chars(name):
    # Choose two random indices to insert the special characters
    special_char_index_1 = random.randint(0, len(name))
    special_char_index_2 = random.randint(0, len(name))
    # Ensure that the indices are not the same
    while special_char_index_1 == special_char_index_2:
        special_char_index_2 = random.randint(0, len(name))
    # Choose two random special characters
    special_char_1 = random.choice(['#', '@', '!', 
                                  '$', '%', '^', 
                                  '&', '*'])
    special_char_2 = random.choice(['#', '@', '!', 
                                  '$', '%', '^', 
                                  '&', '*'])
    # Insert the special characters into the name string
    if special_char_index_1 < special_char_index_2:
        modified_name = name[:special_char_index_1] + special_char_1 + name[special_char_index_1:special_char_index_2] + special_char_2 + name[special_char_index_2:]
    else:
        modified_name = name[:special_char_index_2] + special_char_2 + name[special_char_index_2:special_char_index_1] + special_char_1 + name[special_char_index_1:]
    return modified_name

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
   final_name = add_special_chars(active_name)
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)

   
   
   
   