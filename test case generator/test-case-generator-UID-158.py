# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-158' 
theme = 'Name Part Variations'
category = 'Number Replacement'
sub_category = '>2 strings replaced by number'
entity_type = 'Entity'

# ********************

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd

def replace_strings_with_number(name):
    # Define a dictionary of string-number replacements
    replacements = {
        'ONE': '1',
        'TWO': '2',
        'THREE': '3',
        'FOUR': '4',
        'FIVE': '5',
        'SIX': '6',
        'SEVEN': '7',
        'EIGHT': '8',
        'NINE': '9',
        'TEN': '10'
    }
    # Split the name into words
    words = name.split()
    # Loop over the words and replace any string that matches a key in the replacements dictionary with the corresponding value
    for i in range(len(words)):
        if words[i] in replacements:
            words[i] = replacements[words[i]]
    # Join the words back together with spaces
    modified_name = ' '.join(words)
    return modified_name

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
   
    # replace > 2 strings with a number in the name
    modified_name = replace_strings_with_number(row['name']) 
    
    # construct the test case name
    final_test_name = modified_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe
    
print(final_test_cases)
