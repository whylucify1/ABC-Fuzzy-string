# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-120' 
theme = 'Different Name Parts'
category = 'Last Name Part'
sub_category = '1 Name Part difference'
entity_type = 'entity'

# ********************

#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


#%%

import random

def change_text(text, similar_words):
    # Split the text into words
    words = text.split()

    # Choose a random similar word to the last word
    new_word = random.choice(similar_words)

    # Replace the last word with the new word
    words[-1] = new_word

    # Join the words back together into a single string
    new_text = " ".join(words)

    return new_text


# List of similar words
similar_words = ["Development", "Innovation", "Progress", "Advancement", "Growth", "Registration"]


#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

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
    text = row['name']
    final_test_name = change_text(text, similar_words)
    final_test_name = final_test_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
    

#%%

final_test_cases.to_csv('new csv files/120.csv', index=False)  
