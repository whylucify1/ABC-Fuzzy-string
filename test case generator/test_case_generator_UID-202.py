# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-202' 
theme = 'Names where name parts are modified'
category = 'Character Replaced by Number'
sub_category = '1 Letter Replaced by Number'
entity_type = 'Entity'

# ********************

#%%
#import numpy as np
#x = 5 # change when you want different results
#np.random.seed(x)
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

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)


#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
#run loop to generate the test cases 
import random
import string

for index, row in ofac_list_sampled.iterrows():
   active_name = row['name']
   name = active_name
   index = random.randint(0, len(name))  # select a random index in the name
   final_name = name[:index-1] + random.choice('123456789') + name[index:]
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)


#%%

final_test_cases.to_csv('new csv files/202.csv', index=False)   