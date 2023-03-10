# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-279' 
theme = 'Names where Name Parts are Modified'
category = 'Truncation'
sub_category = '2 Letter Truncation in a middle name part'
entity_type = 'Entity'

# ********************

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_2

def truncate_middle_name_2(name, num_letters_to_truncate=2):
    # Separate the name into words
    words = name.split()
    # Check if the name has a middle name (i.e., if it has more than two words)
    if len(words) > 2:
        # Truncate the second-to-last word by removing the last two characters
        truncated_word = words[-2][:-num_letters_to_truncate]
        # Replace the original second-to-last word with the truncated word
        words[-2] = truncated_word
        # Join the words back together with spaces
        truncated_name = ' '.join(words)
    else:
        # If the name doesn't have a middle name, return the original name
        truncated_name = name
    return truncated_name

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

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

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

# run loop to generate the test cases

for index, row in ofac_list_sampled.iterrows():
   
    # truncate a random middle name by two letters
    modified_name = truncate_middle_name_2(row['name']) 
    
    # construct the test case name
    final_test_name = modified_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe
    
print(final_test_cases)
