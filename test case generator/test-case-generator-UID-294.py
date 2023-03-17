uid = 'UID-294'
theme = 'Names where Name Parts are Modified'
category = 'Typos'
sub_category = '> 2 Typos same name part - Adjacent,at the end'
entity_type = 'Entity'

import pandas as pd
import random
import string

def insert_adjacent_typos_at_end(name, n_typos):
    words = name.split(' ')
    last_word = words[-1]
    
    for _ in range(n_typos):
        typo_index = random.randint(len(last_word) - 2, len(last_word) - 1)
        typo_letter = random.choice(string.ascii_letters)
        last_word = last_word[:typo_index] + typo_letter + last_word[typo_index + 1:]
    
    modified_name = ' '.join(words[:-1]) + ' ' + last_word
    return modified_name.upper()

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')]
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = insert_adjacent_typos_at_end(row['name'], 3)
    final_test_name = modified_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
