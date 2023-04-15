# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-372' 
theme = 'Special Characters and Spaces'
category = 'Removal'
sub_category = '1 special characters removed'
entity_type = 'individual'

# ********************

#%%
import numpy as np
x = 8 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_2, separate_words_in_name_3
import re



# Download the OFAC list from the web
ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

# Filter for individuals
ofac_list_filtered = ofac_list[ofac_list.entity_type == 'individual']  # Corrected filter

# Filter for names with exactly one special character
def has_one_special_char(name):
    special_chars = re.findall(r'[^\w\s]', name)
    return len(special_chars) == 1

ofac_list_filtered_one_special_char = ofac_list_filtered[ofac_list_filtered['name'].apply(has_one_special_char)]

# Randomly choose 500 rows or the total number of rows if there are less than 500 rows
num_rows = ofac_list_filtered_one_special_char.shape[0]
num_samples = min(500, num_rows)
ofac_list_sampled = ofac_list_filtered_one_special_char.sample(n=num_samples)

# Print the sampled DataFrame
print(ofac_list_sampled)

# ---------------------
# CREATE THE TEST CASES
# ---------------------

import random


def remove_special_chars(name):
    # find all special characters in the entity name
    special_chars = re.findall(r'[^\w\s]', name)

    # check if there is special characters  
    if len(special_chars) >=1:
            # remove the 3 special characters
        name = re.sub(r'[^\w\s]', '', name, count=1)
        

    return name



# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    

        
    final_test_name=remove_special_chars(row['name'])
        
        
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
    print(final_test_name)
        


final_test_cases[['Sub-category', 'Original Name', 'Test Case Name']].to_csv('test_cases_372.csv', index=False, header=['Test Type', 'Original Name', 'Altered Name'])


        