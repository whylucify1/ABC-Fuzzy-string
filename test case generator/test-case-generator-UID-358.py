uid = 'UID-358'
theme = 'Special Characters and Spaces'
category = 'Compression'
sub_category = 'Compress common and non common name parts'
entity_type = 'Entity'

import pandas as pd
import re

def compress_name_parts(name):
    name_parts = re.split(r'\s+', name)
    compressed_name_parts = [name_parts[0]]
    for part in name_parts[1:]:
        if part[0].isalnum():
            compressed_name_parts[-1] += part
        else:
            compressed_name_parts.append(part)
    return ' '.join(compressed_name_parts).upper()

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[ofac_list.entity_type == '-0- ']
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID', 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = compress_name_parts(row['name'])
    final_test_name = modified_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
