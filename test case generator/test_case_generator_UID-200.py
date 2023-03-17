
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-200' 
theme = 'Names where Name Parts are Modified'
category = 'Character Replaced by Number'
sub_category = '>2 Letters Replaced by Numbers - same name part'
entity_type = 'individual'

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

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

import random



# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    if number_of_words_first_middle != 1:
        separated_words = separate_words_in_name_3(row['name']) # separate the name into distinct words
        

        name = separated_words[1]
        indices = random.sample(range(len(name)), 3)  # select 3 random indices
        
        modified_name = ""
        for i in range(len(name)):
            if i in indices:
                modified_name += str(random.randint(0, 9))  # replace character with random digit
            else:
                modified_name += name[i]
        
        

        final_test_name = separated_words[0] + ' ' + modified_name + ' ' + separated_words[2] + '.'  #create the test case        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
        
    else: 
        separated_words = separate_words_in_name_2(row['name']) # separate the name into distinct words

        
        
        name = separated_words[1]
        indices = random.sample(range(len(name)), 3)  # select 3 random indices
        
        modified_name = ""
        for i in range(len(name)):
            if i in indices:
                modified_name += str(random.randint(0, 9))  # replace character with random digit
            else:
                modified_name += name[i]
        

    
        final_test_name = separated_words[0] + ' ' + modified_name + '.'  #create the test case        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
        
        
        