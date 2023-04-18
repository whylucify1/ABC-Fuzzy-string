# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-399' 
theme = 'Special Characters and Spaces'
category = 'Split'
sub_category = 'Split noise name parts'
entity_type = 'entity'


# ********************

#%%
#import numpy as np
#x = 6 # change when you want different results
#np.random.seed(x)
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

import pandas as pd

noise_words = ['at', 'and', 'name', 'the', 'with', 'in', 'on', 'for', 'to']

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    name = row['name']
    words = name.split()
    new_words = []
    for word in words:
        if word.lower() in noise_words:
            new_word = word[:-2] + " " + word[-2:]
        else:
            new_word = word
        new_words.append(new_word)
    final_test_name = " ".join(new_words).upper()
    if any(word.lower() in noise_words for word in name.lower().split()):
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], name, final_test_name]
    print(final_test_name)

#%%

final_test_cases.to_csv('new csv files/399.csv', index=False)   