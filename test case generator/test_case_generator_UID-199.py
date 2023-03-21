# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-199' 
theme = 'Names where name parts are Modified'
category = 'Character Replaced by Number'
sub_category = '> 2 Letters replaced by numbers - same name part'
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
# CREATE THE RANDOM NUMBER FUNCTION
# ---------------------

import random
import string


def replace_random_numbers(name):
    # Split the input string into a list of words
    words = name.split()
    
    # Select a random word from the list
    selected_word = random.choice(words)
    
    # Generate 3 random digits
    random_numbers = [str(random.randint(0, 9)) for _ in range(3)]
    
    # Select random positions within the word to replace with the digits
    word_len = len(selected_word)
    if word_len >= 3:
        positions = sorted(random.sample(range(word_len), 3))
    else:
        positions = range(word_len)
    
    # Replace the characters at the selected positions within the word with the digits
    new_word = ''
    for i in range(word_len):
        if i in positions:
            new_word += random_numbers[positions.index(i)]
        else:
            new_word += selected_word[i]
    
    # Replace the selected word with the new word in the input string
    new_name = name.replace(selected_word, new_word)
    
    return new_name

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    name = row['name']
  
    final_test_name=replace_random_numbers(name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]

    print(final_test_name)