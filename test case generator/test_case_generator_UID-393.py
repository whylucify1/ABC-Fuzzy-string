# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-393' 
theme = 'Special Characters and Spaces'
category = 'Split'
sub_category = 'All name parts split'
entity_type = 'individual'

def random_space(name):
    import random
    name = name.replace(",", "")
    words = name.split()
    for i in range(len(words)):
        if len(words[i]) > 1:
            index = random.randint(1, len(words[i]) - 1)
            words[i] = words[i][:index] + " " + words[i][index:]
    return " ".join(words)

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
from test_case_generator_functions import random_space
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
for index, row in ofac_list_sampled.iterrows():
    names = row['name']
    last_name, first_name = names.split(", ")
    final_test_name = first_name + ' ' + last_name
    final_test_name = random_space(final_test_name)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
