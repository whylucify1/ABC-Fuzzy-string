# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-132' 
theme = 'Name Part Variations'
category = 'Company designator variation'
sub_category = '2 Company designator equivalent'
entity_type = 'entity'

# ********************

#%%
#import numpy as np
#x = 6 # change when you want different results
#np.random.seed(x)
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
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)



#%%

import random

def change_designators(text, designators):
    """
    This function replaces one designator in a given string with a random designator from the list of designators.
    """
    new_designator = random.choice(designators)
    for designator in designators:
        if designator in text:
            while new_designator == designator:
                new_designator = random.choice(designators)
            text = text.replace(designator, new_designator, 1)
            break  # replace only one designator per iteration
    return text


designators = ['INC.', 'PTE', 'LTD', 'LLC', 'CO.', 'CORP.', 'GMBH', 'S.A.', 'B.V.', 'AB', 'A/S', 'S.R.L.',
               'OY', 'PTY. LTD.', 'PLC', 'LLP','BVBA', 'S.A.S.', 'K.K.', 'SDN. BHD.', 'LTDA.', 'SA/NV', 'S.A.R.L.U.', 'ASBL', 'K.S.', 'S.A. DE C.V.',
               'LIMITED', 'S. DE H.', 'S.C.S.', 'E.U.', 'GMBH & CO. KG', 'LLC & CO. KG', 'PTY LTD', 'SP. Z O.O.']

#%%

# create blank final test cases table
final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

# run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    names = row['name']
    final_test_name = change_designators(names, designators)
    final_test_name = final_test_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]
    print(final_test_name)
 
    
#%%

final_test_cases.to_csv('new csv files/132.csv', index=False)      