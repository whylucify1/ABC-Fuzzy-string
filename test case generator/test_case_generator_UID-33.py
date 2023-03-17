# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-33' 
theme = 'Name Additions'
category = 'Last Name Part'
sub_category = '1 Name Part added twice'
entity_type = 'entity'

# ********************

#%%

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_2, separate_words_in_name_3
# download the OFAC list from the web


# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

import random
# Define a list of last names
last_names = ['Smith', 'Johnson', 'Williams', 
              'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 
              'Moore', 'Taylor', 'Anderson', 'Jackson', 'Parker', 
              'White', 'Harris', 'Clark', 'Lewis', 'Allen', 'Scott', 'Young']

# Choose a random last name from the list




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
    

    busdes_name = row['name']
    random_last_name1 = random.choice(last_names)
    random_last_name2 = random.choice(last_names)
    
    final_test_name = busdes_name+' '+random_last_name1+' '+random_last_name2
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
    print(final_test_name)
    
    
    