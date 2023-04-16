# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-339' 
theme = 'Special Characters and Spaces'
category = 'Additional noise'
sub_category = 'Additional noise in between'
entity_type = 'Entity'

# ********************
#%%
#import numpy as np
#x = 5 # change when you want different results
#np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd

import random

def add_noise_between_words(input_string, n_noise):
    # Split the input string into a list of words
    words = input_string.split()
    
    # Define a list of possible noise words to insert between the words
    noise_words = ['at', 'name', 'the', 'of', 'with', 'in', 'on', 'for', 'to']
    
    # Add the specified number of noise elements between words
    for i in range(n_noise):
        # Choose a random index to insert the noise element
        index = random.randint(1, len(words))
        
        # Choose a random noise element from the list of possible noise words
        noise = random.choice(noise_words)
        
        # Insert the noise element at the chosen index
        words.insert(index, noise)
    
    # Join the modified list of words back into a string and return it
    return ' '.join(words).upper()


#%%

# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


#%%
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

# run loop to generate the test cases

for index, row in ofac_list_sampled.iterrows():
    
    final_name = add_noise_between_words(row['name'], 2)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + '-' + str(index), row['uid'], row['name'], final_name]
print(final_test_cases)

#%%

final_test_cases.to_csv('new csv files/339.csv', index=False)   