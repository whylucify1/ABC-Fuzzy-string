# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-196' 
theme = 'Names where name parts are Modified'
category = 'Character Replaced by Number'
sub_category = '>2 Letters replaced by numbers - different name part'
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



def replacement_three_number(name):
    # select three random indices 
    valid_indices = [i for i in range(len(name)) if name[i].isalpha()]
    
    index1, index2, index3 = random.sample(valid_indices, 3)
    
    while index1 == index2 or index1 == index3 or index2 == index3:
        index1, index2, index3 = random.sample(valid_indices, 3)

    
    random_number1 = random.randint(0, 9)
    random_number2 = random.randint(0, 9)
    random_number3 = random.randint(0, 9)
    
    
    sort_index=sorted([index1, index2, index3])
    
    
    index1, index2, index3=sort_index[0], sort_index[1], sort_index[2]
    
    
    new_name = name[:index1] + str(random_number1) + name[index1+1:index2] + str(random_number2) + name[index2+1:index3]+str(random_number3)+name[index3+1:]
   
    
    
    return new_name


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
    ########
    
    
   #final_test_name = " ".join([first_word] + middle_words + [last_word])
    
    
    final_test_name=replacement_three_number(busdes_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]

    print(final_test_name)
    