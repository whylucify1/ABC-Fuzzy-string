uid = 'UID-250'
theme = 'Names where Name Parts are Modified'
category = 'Transpositions'
sub_category = '1 transposition - more than 2 letters anywhere'
entity_type = 'Entity'

import pandas as pd
import random

def transpose_more_than_2_letters(name):
    words = name.split(' ')
    selected_word_indices = random.sample(range(len(words)), 2)
    i, j = random.sample(range(len(words[selected_word_indices[0]])), 1)[0], random.sample(range(len(words[selected_word_indices[1]])), 1)[0]
    words[selected_word_indices[0]], words[selected_word_indices[1]] = list(words[selected_word_indices[0]]), list(words[selected_word_indices[1]])
    words[selected_word_indices[0]][i], words[selected_word_indices[1]][j] = words[selected_word_indices[1]][j], words[selected_word_indices[0]][i]
    words[selected_word_indices[0]], words[selected_word_indices[1]] = "".join(words[selected_word_indices[0]]), "".join(words[selected_word_indices[1]])
    return " ".join(words)

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')]
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = transpose_more_than_2_letters(row['name'])
    final_test_name = modified_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
