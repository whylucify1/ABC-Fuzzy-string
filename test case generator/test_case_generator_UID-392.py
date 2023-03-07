
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-392' 
theme = 'Special Characters and Spaces'
category = 'Split'
sub_category = 'All name parts split'
entity_type = 'entity'

def bus_random_space(name):
    import random
    words = name.split()
    for i, word in enumerate(words):
        if len(word) > 1:
            index = random.randint(1, len(word) - 1)
            words[i] = word[:index] + ' ' + word[index:]
    new_name = ' '.join(words)
    return new_name.upper()

# ********************

#%%
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import bus_random_space

# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate individuals
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
    org_name = row['name']
    final_test_name = bus_random_space(org_name)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)