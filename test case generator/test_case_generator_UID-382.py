# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-382' 
theme = 'Special Characters and Spaces'
category = 'Split'
sub_category = '> 2 name parts split'
entity_type = 'individual'


import random



def random_space1(name):
    name = name.replace(",", "")
    # Split the name into first name, middle name, and last name
    words = name.split()
    first_name = words[0]
    middle_name = None
    last_name = None
    if len(words) > 1:
        last_name = words[-1]
    if len(words) > 2:
        middle_name = " ".join(words[1:-1])
    # Insert a random space in each of the three name parts
    if first_name:
        index = random.randint(1, len(first_name)-1)
        first_name = first_name[:index] + " " + first_name[index:]
    if middle_name:
        index = random.randint(1, len(middle_name)-1)
        middle_name = middle_name[:index] + " " + middle_name[index:]
    if last_name:
        index = random.randint(1, len(last_name)-1)
        last_name = last_name[:index] + " " + last_name[index:]
    # Combine the parts and return the modified name
    modified_name = first_name
    if middle_name:
        modified_name += " " + middle_name
    if last_name:
        modified_name += " " + last_name
    return modified_name




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
from test_case_generator_functions import random_space1
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate individuals
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') >2)]

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
    final_test_name = random_space1(names)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
