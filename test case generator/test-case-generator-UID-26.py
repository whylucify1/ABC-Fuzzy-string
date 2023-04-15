# ********************
# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-26' 
theme = 'Name additions'
category = 'Last name'
sub_category = '1 Last Name added'
entity_type = 'individual'

# ********************

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

import pandas as pd
import numpy as np
import random
import string

def rand_letter():
    return random.choice(string.ascii_uppercase)

def separate_words_in_name_2(full_name):
    last_name, first_name = full_name.split(', ')
    return [last_name, first_name]

def separate_words_in_name_3(full_name):
    last_name, first_middle_names = full_name.split(', ')
    first_middle_name_parts = first_middle_names.split(' ')
    if len(first_middle_name_parts) == 1:
        return [last_name, first_middle_name_parts[0], ""]
    else:
        return [last_name, first_middle_name_parts[0], first_middle_name_parts[1]]

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

np.random.seed(5)
ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')]
ofac_list_sampled = ofac_list_filtered.sample(n = 500)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    number_of_words = row['name'].count(' ') + 1
    if number_of_words == 2:
        separated_words = separate_words_in_name_2(row['name'])
        last_name = separated_words[0] + " " + rand_letter() + "I"  # Adding 'KI' to the last name
        final_test_name = separated_words[1] + " " + last_name
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]
    else:
        separated_words = separate_words_in_name_3(row['name'])
        last_name = separated_words[0] + " " + rand_letter() + "I"  # Adding 'KI' to the last name
        final_test_name = separated_words[1] + " " + separated_words[2] + " " + last_name if separated_words[2] else separated_words[1] + " " + last_name
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

final_test_cases.to_csv('final_test_cases_26.csv', index=False, columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Original Name', 'Test Case Name'])
