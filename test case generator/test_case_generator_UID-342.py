
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-342' 
theme = 'Special Characters and Spaces'
category = 'Additional Spaces'
sub_category = 'Abnormally large number of spaces between Name Parts'
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
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

import random

def add_spaces_between_spaces(string):
    # Split the string into a list of individual characters
    chars = list(string)
    new_chars = []
    
    # Loop through the characters and insert spaces between pairs of spaces
    for i in range(len(chars)):
        if chars[i] == ' ' and i > 0 and i < len(chars) - 1:
            # Insert a random number of spaces between pairs of spaces
            num_spaces = random.randint(5, 10)
            new_chars.append(' ' * num_spaces)
        else:
            new_chars.append(chars[i])
    
    # Join the modified characters back into a string
    return ''.join(new_chars)






import random

def add_spaces_between_name_parts(name):
    parts = name.split()
    num_parts = len(parts)
    new_parts = []
    for i in range(num_parts):
        new_parts.append(parts[i])
        if i < num_parts - 1:
            num_spaces = random.randint(5, 10)
            new_parts.append(" " * num_spaces)
    return "".join(new_parts)







# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 



for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    if number_of_words_first_middle != 1:
        separated_words = separate_words_in_name_3(row['name']) # separate the name into distinct words
        
        name0=add_spaces_between_spaces(separated_words[0])
        name1=add_spaces_between_spaces(separated_words[1])
        name2=add_spaces_between_spaces(separated_words[2])
        
        
        name=separated_words[0]+' '+separated_words[1]+' '+separated_words[2]
        
      
        final_test_name = add_spaces_between_name_parts(name)+'.'  #create the test case        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
        
    else: 
        separated_words = separate_words_in_name_2(row['name']) # separate the name into distinct words
        
        name=separated_words[0]+' '+separated_words[1]
        
      
        final_test_name = add_spaces_between_name_parts(name)+'.' 
           
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)
        
        
        

final_test_cases[['Sub-category', 'Original Name', 'Test Case Name']].to_csv('test_cases_342.csv', index=False, header=['Test Type', 'Original Name', 'Altered Name'])

