uid = 'UID-96' 
theme = 'Modified Order'
category = 'Given Name'
sub_category = '2 middle names swapped'
entity_type = 'individual'

# ********************

#%%
import numpy as np
x = 7 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------
def separate_words_in_name_4(name):
    first_name = name[name.find(', ')+2:name.find(' ',name.find(', ')+2)]
    middle_name = name[name.find(' ',name.find(', ')+2)+1:]
    last_name = name[:name.find(',')]
    
    if ' ' in middle_name:
        middle_name = middle_name[:middle_name.find(' ')] + ' ' + middle_name[middle_name.find(' ')+1:]
    
    if ' ' in middle_name:
        middle_name_2 = middle_name[middle_name.find(' ')+1:]
        middle_name = middle_name[:middle_name.find(' ')]
    else:
        middle_name_2 = ''
    
    separated_words = [first_name, middle_name, middle_name_2, last_name]
    
    return separated_words

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_4
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate individuals
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') >2)]
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
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    if number_of_words_first_middle >=3 : 
        separated_words = separate_words_in_name_4(row['name'])
        final_test_name = separated_words[0] + " " + separated_words[2] +" " + separated_words[1] + " " + separated_words[3]
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
        print(final_test_name)
    
