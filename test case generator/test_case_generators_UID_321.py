# *********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-321' 
theme = 'Special Characters and Spaces'
category = 'Addition'
sub_category = '>2 special character added'
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




def add_special_chars(name, num_special_chars):
    # Choose random indices to insert the special characters
    special_char_indices = random.sample(range(len(name)), num_special_chars)
    # Choose random special characters
    special_chars = random.choices(['#', '@', '!', 
                                  '$', '%', '^', 
                                  '&', '*'], k=num_special_chars)
    # Sort the indices in ascending order
    special_char_indices.sort()
    # Insert the special characters into the name string
    modified_name = name[:special_char_indices[0]] + special_chars[0]
    for i in range(num_special_chars - 1):
        modified_name += name[special_char_indices[i]:special_char_indices[i+1]] + special_chars[i+1]
    modified_name += name[special_char_indices[num_special_chars-1]:]
    return modified_name

# Example usage:
full_name = 'John Smith'
modified_full_name = add_special_chars(full_name, 3)
print(modified_full_name)
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
   final_name = add_special_chars(active_name, 3)
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)

   
   
   
   
