# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-257' 
theme = 'Names where name parts are Modified'
category = 'Transpositions'
sub_category = '2 transpositions (same name part) '
entity_type = 'entity'

# ********************

#%%
import numpy as np
x = 7 # change when you want different results
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


def entity_name_transposition(entity_name):
    # Split the entity name into words
    words = entity_name.split()

    # Select a random word from the entity name
    selected_word = random.choice(words)
    
    # Transpose two letters in the selected word
    valid_indices = [i for i in range(len(selected_word)) if selected_word[i].isalpha()]
    index1, index2 = random.sample(valid_indices, 2)
    transposed_word = selected_word[:index1] + selected_word[index2] + selected_word[index1+1:index2] + selected_word[index1] + selected_word[index2+1:]
    index3, index4 = random.sample(valid_indices, 2)
    while index3 == index1 or index3 == index2 or index4 == index1 or index4 == index2:
        index3, index4 = random.sample(valid_indices, 2)
    if index3 > index4:
        index3, index4 = index4, index3
    transposed_word = transposed_word[:index3] + transposed_word[index4] + transposed_word[index3+1:index4] + transposed_word[index3] + transposed_word[index4+1:]

    # Replace the selected word with the transposed word in the entity name
    transposed_entity_name = ' '.join([transposed_word if word == selected_word else word for word in words])

    return transposed_entity_name


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
    
    final_test_name = " ".join([first_word] + middle_words + [last_word])
    final_test_name = entity_name_transposition(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    
 
    print(final_test_name)

  
    