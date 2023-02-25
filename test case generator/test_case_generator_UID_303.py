# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-303' 
theme = 'Names where name parts are Modified'
category = 'Typos'
sub_category = '1 typo, first letter'
entity_type = 'indivisual'

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
from test_case_generator_functions import separate_words_in_name_3
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate individuls
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 50)
print(ofac_list_sampled)
#%%
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
           'W', 'X', 'Y', 'Z']
rand_letter = alphabet[random.randrange(1,26)]
#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
    active_name = row['name']
    if rand_letter != active_name[0]:
        final_name = rand_letter + (active_name[1:])
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name] # append to the dataframe
final_test_cases_sampled = final_test_cases.sample(n=10)
print(final_test_cases_sampled)