
# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-238' 
theme = 'Names where name parts are Modified'
category = 'Transpositions'
sub_category = '1 transposition - 2 letters Any where'
entity_type = 'entity'

# ********************

#%%
import numpy as np
x = 2 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_2, separate_words_in_name_3
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



# ---------------------
# CREATE THE TEST CASES
# ---------------------

import random
import string

def transpose_two_letters(entity_name):
    # select two random indices for transposition
    
    valid_indices = [i for i in range(len(entity_name)) if entity_name[i].isalpha()]
    
    index1, index2 = random.sample(valid_indices, 2)
    
    #index1, index2 = random.sample(range(len(entity_name)), 2)
    

    # swap the characters at the selected indices
    transposed_name = entity_name[:index1] + entity_name[index2] + entity_name[index1+1:index2] + entity_name[index1] + entity_name[index2+1:]

    return transposed_name

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    busdes_name = row['name']
    words = busdes_name.split()
    first_word = words[0]
    last_word = words[-1]
    middle_words = words[1:-1]
    
    
    final_test_name=transpose_two_letters(busdes_name)
  
    
    #final_test_name = " ".join([first_word] + middle_words + [last_word])
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]

    print(final_test_name)
    
    
    
    