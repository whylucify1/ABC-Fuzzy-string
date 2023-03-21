# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-379' 
theme = 'Special characters and spaces'
category = 'Replaced by word'
sub_category = 'Special character replaced by full name part'
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

def replace_special_characters(input_string):
    # Define a dictionary with mappings from special characters to full names
    replacements = {'&': 'AND', '$': 'DOLLAR', '@': 'AT', '#': 'HASHTAG', '%': 'PERCENT'}
    
    # Iterate over the characters in the input string and replace any that match
    output_string = ''
    for char in input_string:
        if char in replacements:
            output_string += replacements[char]
        else:
            output_string += char
    
    return output_string

#%%

# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

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

# run loop to generate the test cases

for index, row in ofac_list_sampled.iterrows():

    final_name = replace_special_characters(row['name'])
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + '-' + str(index), row['uid'], row['name'], final_name]
print(final_test_cases)