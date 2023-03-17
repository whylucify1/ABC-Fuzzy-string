uid = 'UID-364'
theme = 'Special Characters and Spaces'
category = 'Different character'
sub_category = '1 special character replaced by equivalent'
entity_type = 'Individual'

import pandas as pd
import random

def replace_special_chars(name, replacements, n_replacements):
    name_list = list(name.upper())
    special_chars_indices = [i for i, c in enumerate(name_list) if c in replacements.keys()]

    if len(special_chars_indices) < n_replacements:
        raise ValueError("Not enough special characters in the name to replace.")

    indices_to_replace = random.sample(special_chars_indices, n_replacements)
    for index in indices_to_replace:
        name_list[index] = replacements[name_list[index]]

    return ''.join(name_list)

replacements = {
    ',': '.',
    '.': ',',
    '-': '_',
    '_': '-',
    '/': '\\',
}

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0, 1, 2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')]
ofac_list_sampled = ofac_list_filtered.sample(n=10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    try:
        modified_name = replace_special_chars(row['name'], replacements, 1)
        final_test_name = modified_name
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]
    except ValueError as e:
        print(f"Skipping {row['name']}: {e}")

print(final_test_cases)
