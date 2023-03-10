# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-150' 
theme = 'Name Part Variations'
category = 'Name Part Abbreviation'
sub_category = '2 name parts abbreviated'
entity_type = 'Entity'

# ********************

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd

# Define a function to abbreviate the first two name parts

def abbreviate_first_two_parts(name):
    words = name.split()
    if len(words) > 2:
        abbreviated_name = words[0][:4].upper() + ' ' + words[1][:2].upper() + ' ' + ' '.join(words[2:])
    else:
        abbreviated_name = name
    return abbreviated_name

# Download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# Filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities

# Randomly choose 10 rows

ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# Create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

# Run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
   active_name = row['name']
   final_name = abbreviate_first_two_parts(active_name)
   final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], active_name, final_name] # append to the dataframe

print(final_test_cases)
