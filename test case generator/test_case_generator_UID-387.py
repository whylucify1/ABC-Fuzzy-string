# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-387' 
theme = 'Special Characters and Spaces'
category = 'Split'
sub_category = '2 name parts split'
entity_type = 'Entity'

def add_random_space(name):
    import random
    words = name.split()
    if len(words) > 1:
        # Select two distinct indices from the words list
        idx1, idx2 = random.sample(range(len(words)), 2)
        # Ensure that the first index is less than the second index
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        # Choose a random index within each selected word
        word1 = words[idx1]
        word2 = words[idx2]
        index1 = random.randint(1, len(word1) - 1)
        index2 = random.randint(1, len(word2) - 1)
        # Insert a space character at the selected indices
        words[idx1] = word1[:index1] + ' ' + word1[index1:]
        words[idx2] = word2[:index2] + ' ' + word2[index2:]
    new_name = ' '.join(words)
    return new_name.upper()



# ********************

#%%
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import add_random_space

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

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
# run loop to generate the test cases
for index, row in ofac_list_sampled.iterrows():
    names = row['name']
    final_test_name = add_random_space(names)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
