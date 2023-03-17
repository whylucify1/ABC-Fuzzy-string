uid = 'UID-243' 
theme = 'Names where Name Parts are Modified'
category = 'Transpositions'
sub_category = '> 2 transpositions (different name part)'
entity_type = 'Entity'

import pandas as pd
import random

def transpose_letters(name, n_transpositions):
    words = name.split(' ')
    modified_words = []
    for word in words:
        word_list = list(word)
        for _ in range(n_transpositions):
            i, j = random.sample(range(len(word_list)), 2)
            word_list[i], word_list[j] = word_list[j], word_list[i]
        modified_words.append("".join(word_list))
    return " ".join(modified_words)

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')]
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = transpose_letters(row['name'], 2)
    final_test_name = modified_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
