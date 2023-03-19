# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-224' 
theme = 'Names where name parts are Modified'
category = 'Repetitions'
sub_category = '> 2 letters repeated once'
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
import re
def repeat_random_letters(name):
    # Convert the name to a list of characters
    name_chars = list(name)
    repeated_letters = set()
    # Choose three random indices with unique letters
    while len(repeated_letters) < 3:
        index = random.randint(0, len(name_chars) - 1)
        if not re.match(r'[A-Za-z]', name_chars[index]):
            continue
        repeated_letters.add(name_chars[index])
    # Repeat each selected letter once or twice and construct the modified name
    for letter in repeated_letters:
        index = name_chars.index(letter)
        repeat_count = random.randint(1, 2)
        name_chars = name_chars[:index+1] + [letter]*repeat_count + name_chars[index+1:]
    new_name = ''.join(name_chars)
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
    
    
    final_test_name=repeat_random_letters(busdes_name)
  
    
    #final_test_name = " ".join([first_word] + middle_words + [last_word])
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]

    print(final_test_name)
    