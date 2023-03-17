
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-345' 
theme = 'Special Characters and Spaces'
category = 'Additional Spaces'
sub_category = 'Abnormally large number of spaces in the name parts'
entity_type = 'individual'

# ********************

#%%
import numpy as np
x = 10 # change when you want different results
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

def add_space(name):
    # Split the name into a list of individual characters
    chars = list(name)
    
    # Generate a random index where the space will be inserted
    index = random.randint(1, len(chars) - 1)
    
    # Insert the space at the random index
    chars[index] = '         ' + chars[index]
    
    # Join the modified characters back into a string
    return ''.join(chars)



# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    if number_of_words_first_middle != 1:
        separated_words = separate_words_in_name_3(row['name']) # separate the name into distinct words
     
        
        final_test_name = add_space(separated_words[0]) + ' ' + separated_words[1] + ' ' + add_space(separated_words[2]) + '.'  #create the test case        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
          
    else: 
        separated_words = separate_words_in_name_2(row['name']) # separate the name into distinct words
        
        final_test_name = separated_words[0] + ' ' + add_space(separated_words[1]) + '.'  #create the test case        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
        