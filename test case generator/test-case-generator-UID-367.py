uid = 'UID-367'
theme = 'Special Characters and Spaces'
category = 'Different character'
sub_category = 'All special characters replaced by equivalent'
entity_type = 'Entity'

import pandas as pd

def replace_all_special_chars(name, replacements):
    name_list = list(name.upper())
    for i, c in enumerate(name_list):
        if c in replacements.keys():
            name_list[i] = replacements[c]
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

ofac_list_filtered = ofac_list[ofac_list.entity_type == '-0- ']
ofac_list_sampled = ofac_list_filtered.sample(n=10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = replace_all_special_chars(row['name'], replacements)
    final_test_name = modified_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
