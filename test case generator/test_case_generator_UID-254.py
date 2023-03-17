# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-254' 
theme = 'Names where Name Parts are Modified'
category = 'Transpositions'
sub_category = '2 transposition - 2 letters Any where'
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

def transpose_two_letters(name):
    # select two random indices for transposition
    
    valid_indices = [i for i in range(len(name)) if name[i].isalpha()]
    
    index1, index2 = random.sample(valid_indices, 2)
    
    #index1, index2 = random.sample(range(len(name)), 2)
    

    # swap the characters at the selected indices
    transposed_name = name[:index1] + name[index2] + name[index1+1:index2] + name[index1] + name[index2+1:]

    return transposed_name



def two_transpose_two_letters(name):
    # select two random indices for transposition
    valid_indices = [i for i in range(len(name)) if name[i].isalpha()]
    
    # First transposition
    index1, index2 = random.sample(valid_indices, 2)
    transposed_name = name[:index1] + name[index2] + name[index1+1:index2] + name[index1] + name[index2+1:]
    
    # Second transposition
    index3, index4 = random.sample(valid_indices, 2)
    while index3 == index1 or index3 == index2 or index4 == index1 or index4 == index2:
        index3, index4 = random.sample(valid_indices, 2)
    if index3 > index4:
        index3, index4 = index4, index3
    transposed_name = transposed_name[:index3] + transposed_name[index4] + transposed_name[index3+1:index4] + transposed_name[index3] + transposed_name[index4+1:]

    return transposed_name

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    if number_of_words_first_middle != 1:
        separated_words = separate_words_in_name_3(row['name']) # separate the name into distinct words
        
        final_test_name = separated_words[0] + ' ' + separated_words[1] + ' ' + separated_words[2] + '.'  #create the test case   
        #final_test_name=transpose_two_letters(final_test_name)
        final_test_name=two_transpose_two_letters(final_test_name)
        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
        
    else: 
        separated_words = separate_words_in_name_2(row['name']) # separate the name into distinct words

    
        final_test_name = separated_words[0] + ' ' + separated_words[1] + '.'  #create the test case   
        
        final_test_name=two_transpose_two_letters(final_test_name)
        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
        
        
        