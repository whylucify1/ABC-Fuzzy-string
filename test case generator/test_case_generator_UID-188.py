# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-188' 
theme = 'Names where Name Parts are Modified'
category = 'Character Addition'
sub_category = 'Very short name'
entity_type = 'entity'

def rand_letter():
	import random
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
							'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	rand_letter = alphabet[random.randrange(0,26)]
	
	return rand_letter

def separate_words_in_name(name):
    # split the name into last name, first name, and middle names
    name_parts = name.split(", ")
    last_name = name_parts[0]
    first_name_middle_names = name_parts[1]
    
    # split the first name and middle names
    first_name_middle_names_parts = first_name_middle_names.split(" ")
    
    # join all the middle names together
    middle_names = " ".join(first_name_middle_names_parts[1:])
    
    # return the last name, first name, and middle names as separate strings
    return last_name, first_name_middle_names_parts[0], middle_names

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name, rand_letter

# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
ofac_list_filtered = ofac_list_filtered[ofac_list_filtered['name'].str.len() < 10]
# randomly choose 10 rows

ofac_list_sampled = ofac_list_filtered.sample(n=10)
print(ofac_list_sampled)

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    busdes_name = row['name']
    words = busdes_name.split()
    words[0] = words[0] + rand_letter()
    final_test_name = " ".join(words)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)