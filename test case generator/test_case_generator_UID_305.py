
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-305' 
theme = 'Names where name parts are modified'
category = 'typos'
sub_category = '2 typos in different name parts'
entity_type = 'individual'

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
from test_case_generator_functions import separate_words_in_name_3
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

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
#run loop to generate the test cases 
import random

for index, row in ofac_list_sampled.iterrows():
   active_name = row['name']
   name_parts = active_name.split()

   # Choose a random name part to modify the first typo
   first_name_part_index = random.randint(0, len(name_parts) - 1)
   first_name_part = name_parts[first_name_part_index]

   # Generate a random index to insert the first typo
   first_typo_index = random.randint(0, len(first_name_part) - 1)

   # Generate a random lowercase letter to insert as the first typo
   first_typo_char = chr(random.randint(97, 122))

   # Insert the first typo character at the chosen index
   first_name_part_with_typo = first_name_part[:first_typo_index] + first_typo_char + first_name_part[first_typo_index+1:]

   # Replace the modified name part in the original name
   name_parts[first_name_part_index] = first_name_part_with_typo
 

   # Choose another random name part to modify the second typo
   second_name_part_index = random.randint(0, len(name_parts) - 1)
   # Make sure it's a different name part than the first
   while second_name_part_index == first_name_part_index:
    second_name_part_index = random.randint(0, len(name_parts) - 1)

   second_name_part = name_parts[second_name_part_index]

   # Generate a random index to insert the second typo
   second_typo_index = random.randint(0, len(second_name_part) - 1)

   # Generate a random lowercase letter to insert as the second typo
   second_typo_char = chr(random.randint(97, 122))

   # Insert the second typo character at the chosen index
   second_name_part_with_typo = second_name_part[:second_typo_index] + second_typo_char + second_name_part[second_typo_index+1:]

   # Replace the modified name part in the original name
   name_parts[second_name_part_index] = second_name_part_with_typo

   # Join the modified name parts back into a full name
   final_name = ' '.join(name_parts)
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe
print(final_test_cases)
