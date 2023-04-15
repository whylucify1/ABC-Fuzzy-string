import numpy as np
import pandas as pd

def abbreviate_middle_name(full_name):
    name_parts = full_name.split(', ')
    last_name = name_parts[0]
    first_middle_names = name_parts[1].split()
    
    if len(first_middle_names) > 1:
        middle_name = first_middle_names[1]
        middle_initial = middle_name[:3].upper()
        first_middle_names[1] = middle_initial
        
    return f"{first_middle_names[0].upper()} {first_middle_names[1].upper()} {last_name.upper()}"

uid = 'UID-153'
theme = 'Name Part Variations'
category = 'Name Part Abbreviation'
sub_category = 'Middle name abbreviation'
entity_type = 'Individual'

np.random.seed(5)

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0, 1, 2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')]
ofac_list_sampled = ofac_list_filtered.sample(n=500)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID' , 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    number_of_words = row['name'].count(' ') + 1
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1

    if number_of_words_first_middle == 2:
        abbreviated_name = abbreviate_middle_name(row['name'])
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], abbreviated_name]
    else:
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], row['name']]

final_test_cases.to_csv('final_test_cases_153.csv', index=False, columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Original Name', 'Test Case Name'])
