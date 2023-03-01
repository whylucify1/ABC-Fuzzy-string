# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-12' 
theme = 'Name Additions'
category = 'Company Designator'
sub_category = '1 Company Designator Added'
entity_type = 'entity'

# ********************
def rand_bus_designator():
    import random
    business_designators = ['INC.', 'PTE', 'LTD', 'LLC', 'CO.', 'CORP.', 'AG', 'GMBH', 
                            'S.A.', 'B.V.', 'AB', 'A/S', 'S.R.L.', 'OY', 'PTY. LTD.', 'PLC', 
                            'LLP', 'SE', 'KK', 'SARL', 'N.V.', 'SA', 'AS', 'OOO', 
                            'KG', 'KFT.', 'APS', 'BVBA', 'S.A.S.', 'K.K.', 'SDN. BHD.', 'LTDA.', 
                            'SA/NV', 'S.A.R.L.U.', 'BHD.', 'ASBL', 'K.S.', 'S.A. DE C.V.', 'LIMITED', 'S. DE H.', 
                            'S.C.S.', 'S.C.', 'E.U.', 'GMBH & CO. KG', 'LLC & CO. KG', 'PTY LTD', 'SP. Z O.O.']
    rand_bus_designator = business_designators[random.randrange(1,47)]
    return rand_bus_designator

#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import rand_bus_designator
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
for index, row in ofac_list_sampled.iterrows():
    busdes_name = row['name']
    final_test_name = busdes_name + ' ' + rand_bus_designator()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
