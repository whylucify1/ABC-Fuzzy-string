# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-398' 
theme = 'Special Characters and Spaces'
category = 'Split'
sub_category = 'Split common and non common name parts'
entity_type = 'entity'


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

def add_splits(input_string):
    # Split the input string into a list of words
    words = input_string.split()

    # Choose two different random indices of words to add splits to
    if len(words) >= 2:
        split_index1, split_index2 = random.sample(range(len(words)), k=2)
        
        # Split the first word at the midpoint and insert a space
        word1 = words[split_index1]
        if len(word1) > 1:
            midpoint1 = len(word1) // 2
            words[split_index1] = word1[:midpoint1] + ' ' + word1[midpoint1:]
        
        # Split the second word at a random index and insert a space
        word2 = words[split_index2]
        if len(word2) > 1:
            split_point2 = random.randint(1, len(word2) - 1)
            words[split_index2] = word2[:split_point2] + ' ' + word2[split_point2:]
        
    # Join the words back together into a single string
    output_string = ' '.join(words)
    
    return output_string


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
 
    final_test_name = add_splits(row['name'])
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    
    print(final_test_name)

#%%

final_test_cases.to_csv('new csv files/398.csv', index=False)   