uid = 'UID-317'
theme = 'Names where Name Parts are Modified'
category = 'Typos'
sub_category = 'Very Short Name'
entity_type = 'Individual'

import pandas as pd
import random
import string

def insert_typo_very_short_name(name):
    words = name.split(' ')
    last_word = words[-1]
    
    typo_index = random.randint(0, len(last_word) - 1)
    typo_letter = random.choice(string.ascii_letters)
    last_word = last_word[:typo_index] + typo_letter + last_word[typo_index + 1:]
    
    modified_name = ' '.join(words[:-1]) + ' ' + last_word
    return modified_name.upper()

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual') & (ofac_list.name.str.count(' ') < 2)]
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = insert_typo_very_short_name(row['name'])
    final_test_name = modified_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
