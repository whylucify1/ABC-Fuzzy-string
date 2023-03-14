uid = 'UID-135' 
theme = 'Name Part Variations'
category = 'initials'
sub_category = '> 2 middle name initial'
entity_type = 'individual'

# ********************

#%%
import numpy as np
x = 7 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

def separate_words_in_name_5(name):
    first_name = name[name.find(', ') + 2:name.find(' ', name.find(', ') + 2)]
    last_name = name[:name.find(',')]
    
    middle_name = name[name.find(' ', name.find(', ') + 2) + 1:]
    second_space = middle_name.find(' ')
    third_space = middle_name.find(' ', second_space + 1)
    fourth_space = middle_name.find(' ', third_space + 1)
    
    if third_space != -1 and fourth_space != -1:
        # There are at least three middle names, so extract the third and fourth middle names
        third_middle_name = middle_name[third_space + 1:fourth_space]
        fourth_middle_name = middle_name[fourth_space + 1:]
        # Extract the first, second, and third middle names
        second_middle_name = middle_name[second_space + 1:third_space]
        first_middle_name = middle_name[:second_space]
    elif third_space != -1:
        # There are exactly three middle names, so the fourth middle name is an empty string
        third_middle_name = middle_name[third_space + 1:]
        fourth_middle_name = ""
        # Extract the first, second, and third middle names
        second_middle_name = middle_name[second_space + 1:third_space]
        first_middle_name = middle_name[:second_space]
    else:
        # There are not at least three middle names, so all middle names are empty strings
        first_middle_name = ""
        second_middle_name = ""
        third_middle_name = ""
        fourth_middle_name = ""
    
    separated_words = [first_name, first_middle_name, second_middle_name, third_middle_name, fourth_middle_name, last_name]
    return separated_words

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_5
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
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') >3)]
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
    
    if number_of_words_first_middle >3 : 
        separated_words = separate_words_in_name_5(row['name'])
        abbreviated_middle_name1 = separated_words[1][0] + '.'
        abbreviated_middle_name2 = separated_words[2][0] + '.'
        abbreviated_middle_name3 = separated_words[3][0] + '.'
        final_test_name = separated_words[0] + " " + abbreviated_middle_name1 + " " + abbreviated_middle_name2 + " " + abbreviated_middle_name3 + " " + separated_words[4]+" " + separated_words[5]
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
        print(final_test_name)
