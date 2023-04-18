

# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-55' 
theme = 'Name deletions'
category = 'Company Designator'
sub_category = '1 Company designator removed'
entity_type = 'Entity'

# ********************

#%%

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

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate individuals
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') < 3)] # only evaluate names with two or three words

# randomly choose 10 rows

ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)
#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

import re

# run loop to generate the test cases

for index, row in ofac_list_sampled.iterrows():
    company_name = row['name']
    # Define the pattern to match the designator:
    pattern = re.compile(r"\b(?:inc\.?|ltd\.?|limited\.?|corp\.?|ltda\.?|co\.?|llc\.?|plc\.?|llc\.?|gmbh\.?|s\.?a\.?|a\.?s\.?|s\.?r\.?l\.?)\b", flags=re.IGNORECASE)
    final_name = pattern.sub("", company_name)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + '-' + str(index), row['uid'], row['name'], final_name]
print(final_test_cases)
final_test_cases.to_csv('final_test_cases_55.csv', index=False, columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Original Name', 'Test Case Name'])
