# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-399' 
theme = 'Special Characters and Spaces'
category = 'Split'
sub_category = 'Split noise name parts'
entity_type = 'entity'


# ********************

#%%
import numpy as np
x = 6 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd

def split_noise_words(name):
    noise_words = ['at', 'and', 'name', 'the', 'of', 'with', 'in', 'on', 'for', 'to']
    words = name.split()
    for i, word in enumerate(words):
        if word.lower() in noise_words:
            words[i] = word[:-2] + " " + word[-2:]
    return ' '.join(words)

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

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
 
    final_test_name = split_noise_words(row['name'])
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    
 
    print(final_test_name)
