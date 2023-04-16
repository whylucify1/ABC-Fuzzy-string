# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-347' 
theme = 'Special Characters and Spaces'
category = 'Addition'
sub_category = 'Very Short Names w/ Special Character in the Middle'
entity_type = 'entity'


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

import random

def add_special_character(sentence):
    """
    Splits the sentence into words and adds a random special character
    in the middle of words that are six letters or shorter, only if the
    overall length of the sentence is less than or equal to 10 letters.
    """
    special_chars = ["@", "#", "$", "&", "*"]
    words = sentence.split()
    new_words = []
    sentence_length = sum(len(word) for word in words)
    if sentence_length <= 10:
        for word in words:
            if len(word) <= 6:
                special_char = random.choice(special_chars)
                mid_index = len(word) // 2
                word = word[:mid_index] + special_char + word[mid_index:]
            new_words.append(word)
        return " ".join(new_words)
    else:
        return sentence

#%%

# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

# filter for the requirements of the specific test case type


ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases

for index, row in ofac_list_sampled.iterrows():
 
    final_test_name = add_special_character(row['name'])
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
 
    print(final_test_name)

#%%

final_test_cases.to_csv('new csv files/347.csv', index=False)   