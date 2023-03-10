# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-152' 
theme = 'Name Part Variations'
category = 'Name Part Abbreviation'
sub_category = 'First name abbreviation'
entity_type = 'Individual'

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

def abbreviate_first_name(full_name):
    name_parts = full_name.split()
    if len(name_parts) > 2:
        first_name = name_parts[0]
        first_initial = first_name[0].upper() + "."
        name_parts[0] = first_initial
    return " ".join(name_parts)

# download the OFAC list from the web
ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type
ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate individuals
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table
final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    active_name = row['name']
    final_name = abbreviate_first_name(active_name)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_name.upper()] # append to the dataframe

print(final_test_cases)
