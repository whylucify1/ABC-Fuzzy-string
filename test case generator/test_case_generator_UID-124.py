# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-124' 
theme = 'Different Name Parts'
category = 'Name Parts in the middle'
sub_category = '1 Name Part difference'
entity_type = 'entity'

# ********************

#%%
#import numpy as np
#x = 5 # change when you want different results
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


#%%

def rand_name():
	import random
	names = ['Ibrahim','Hashim','Kim','Gonzalez','Ali','Vinko','Dragomir','Roberto','Felix','Edgar','Patrick','Talal','Mario',
							'Carlos','Sergei','Omar','Jong','Richard','Sohrab','Chan','Francisco','Valencia','Ashraf','Sultan','Charles']
	rand_name = names[random.randrange(1,25)]
	
	return rand_name

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
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
    words = busdes_name.split()
    first_word = words[0]
    if len(words) >= 2:
        second_word = words[1]
    else:
        second_word = ""
    final_test_name = [first_word, rand_name()] + words[2:]
    final_test_name = " ".join(final_test_name)
    final_test_name = final_test_name.title()
    final_test_name = final_test_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
    
    
#%%

final_test_cases.to_csv('new csv files/124.csv', index=False)      