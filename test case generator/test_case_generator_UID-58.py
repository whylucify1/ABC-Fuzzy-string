uid = 'UID-58' 
theme = 'Name Deletions'
category = 'First and Last Name'
sub_category = '1 First Name and 1 Last Name removed'
entity_type = 'Individual'

# ********************
def separate_words_in_name_7(name):
    first_name = name[name.find(', ')+2:name.find(' ',name.find(', ')+2)]
    middle_name = name[name.find(' ',name.find(', ')+2)+1:]
    last_name = name[:name.find(',')]
    last_name_parts = last_name.split(" ")
    
    last_name_part1 = last_name_parts[0] if len(last_name_parts) >= 1 else ""
    last_name_part2 = last_name_parts[1] if len(last_name_parts) >= 2 else ""
    last_name_part3 = last_name_parts[2] if len(last_name_parts) >= 3 else ""
    last_name_part4 = last_name_parts[3] if len(last_name_parts) >= 4 else ""
    
    # Split the first name into two name parts
    first_name_parts = first_name.split(" ")
    first_name_part1 = first_name_parts[0] if len(first_name_parts) >= 1 else ""
    first_name_part2 = first_name_parts[1] if len(first_name_parts) >= 2 else ""
    
    return [first_name_part1, first_name_part2, middle_name, last_name_part1, last_name_part2, last_name_part3, last_name_part4]

#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_7
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
    
    if number_of_words_last !=1 : 
        separated_words = separate_words_in_name_7(row['name'])
        final_test_name = separated_words[1] + " " + separated_words[2] +" " + separated_words[4] +" " + separated_words[5] +" " + separated_words[6] 
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
        print(final_test_name)
    
