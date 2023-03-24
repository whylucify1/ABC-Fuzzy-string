# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-131' 
theme = 'Name Part Variations'
category = 'Company designator variation'
sub_category = '1 Company designator equivalent'
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


# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)



#%%

def change_designator(text, designators):
    """
    This function replaces a list of designators in a given string with their abbreviations.
    """
    for designator in designators:
        text = text.replace(designator, designator_abbr(designator))
    return text

def designator_abbr(designator):
    """
    This function returns the abbreviation for a given designator.
    """
    if designator == 'COMPANY':
        return 'Co.'
    else:
        return designator

designators = ['COMPANY', 'CORPORATION', 'INCORPORATED', 'LIMITED']


#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    text = row['name']
    final_test_name = change_designator(text, designators)
    final_test_name = final_test_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
    
    