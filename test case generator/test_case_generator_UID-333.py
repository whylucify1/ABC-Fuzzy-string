# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-333' 
theme = 'Special Characters and Spaces'
category = 'Addition'
sub_category = 'All name parts separated by character'
entity_type = 'individual'

# ********************
def replace_spaces_with_special_character(name, special_characters='@#$%^&*()'):
    import re
    import random
    rand_special_character = random.choice(special_characters)
    name_parts = [part.strip() for part in name.split(',')]
    last_name = name_parts[0].split()[-1]
    first_name = name_parts[1].split()[0]
    middle_names = ' '.join(name_parts[1].split()[1:] + name_parts[2:])
    
    name = re.sub(r'[^\w\s]+', '', name) # remove special characters
    name = name.replace(' ', rand_special_character) # replace spaces
    
    if len(name_parts[0].split()) > 1:
        second_name = name_parts[0].split()[0]
        name = f"{first_name}{rand_special_character}{middle_names}{rand_special_character}{second_name}{rand_special_character}{last_name}"
    else:
        name = f"{first_name}{rand_special_character}{middle_names}{rand_special_character}{last_name}"
    
    return name.upper()
#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import replace_spaces_with_special_character
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
    name = row['name']
    final_test_name = replace_spaces_with_special_character(name)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]
    print(final_test_name)