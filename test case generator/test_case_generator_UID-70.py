# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-70' 
theme = 'Name deletions'
category = 'Last Name Part'
sub_category = '>2 Name Parts removed'
entity_type = 'Entity'

# ********************

def remove_final_three_words(text):
    words = text.split()
    new_words = words[:-3] if len(words) > 3 else []
    return " ".join(new_words)


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

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') >3)]

# randomly choose 10 rows

ofac_list_sampled = ofac_list_filtered.sample(n = 500)
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
    final_test_name = remove_final_three_words(names)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
#%%
final_test_cases.to_csv('70.csv', index=False)   