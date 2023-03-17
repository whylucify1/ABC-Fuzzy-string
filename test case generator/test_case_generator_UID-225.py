# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-225' 
theme = 'Names where name parts are Modified'
category = 'Repetitions'
sub_category = '> 2 letters repeated once'
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


def repeat_random_letters(name):
    # Convert the name to a list of characters
    name_chars = list(name)
    # Choose three random indices
    indices = random.sample(range(len(name_chars)), 3)
    # Repeat the selected letters and construct the modified name
    for index in sorted(indices, reverse=True):
        letter = name_chars[index]
        name_chars = name_chars[:index+1] + [letter] + name_chars[index+1:]
    new_name = ''.join(name_chars)
    return new_name



# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    if number_of_words_first_middle != 1:
        separated_words = separate_words_in_name_3(row['name']) # separate the name into distinct words
        
       
        final_test_name = separated_words[0] + ' ' + separated_words[1] + ' ' + separated_words[2] + '.' 
        
        final_test_name=repeat_random_letters(final_test_name)
        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
    else: 
        separated_words = separate_words_in_name_2(row['name']) # separate the name into distinct words
       
        final_test_name = separated_words[0] + ' ' + separated_words[1] +  '.' 
        
        final_test_name=repeat_random_letters(final_test_name)
        
        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        