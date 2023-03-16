# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-341' 
theme = 'Special Characters and Spaces'
category = 'Additional Spaces'
sub_category = 'Abnormally large number of spaces between Name Parts'
entity_type = 'Entity'

import random
def add_random_space2(name, space_lengths=[4,5,6,7,8]):
    words = name.split()
    formatted_name = ""
    for i, word in enumerate(words):
        formatted_name += word
        if i < len(words) - 1:
            formatted_name += " " * random.choice(space_lengths)
    return formatted_name


# ********************

#%%
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import add_random_space2

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
# run loop to generate the test cases
for index, row in ofac_list_sampled.iterrows():
    names = row['name']
    final_test_name = add_random_space2(names)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
