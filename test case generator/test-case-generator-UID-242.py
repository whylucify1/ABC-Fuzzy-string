uid = 'UID-242' 
theme = 'Names where Name Parts are Modified'
category = 'Repetitions'
sub_category = 'Very Short Name'
entity_type = 'Individual'


import pandas as pd
from test_case_generator_functions import separate_words_in_name_2

def repeat_first_name(name):
    separated_words = separate_words_in_name_2(name)
    modified_name = separated_words[0] + separated_words[0][-1] + ' ' + separated_words[1]
    return modified_name.upper()

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual') & (ofac_list.name.str.count(' ') < 2)]
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = repeat_first_name(row['name'])
    final_test_name = modified_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
