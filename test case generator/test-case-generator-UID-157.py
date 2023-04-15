import pandas as pd
import re

def count_numbers(name):
    return len(re.findall(r'\d+', str(name)))

def replace_numbers(name, num_str_map):
    numbers = re.findall(r'\d+', str(name))
    for num in numbers:
        name = name.replace(num, ''.join([num_str_map[digit] for digit in num]))
    return name

uid = 'UID-157'
theme = 'Name Part Variations'
category = 'Number Replacement'
sub_category = '> 2 numbers replaced by strings'
entity_type = 'Entity'

num_str_map = {
    '0': 'ZERO ',
    '1': 'ONE ',
    '2': 'TWO ',
    '3': 'THREE ',
    '4': 'FOUR ',
    '5': 'FIVE ',
    '6': 'SIX ',
    '7': 'SEVEN ',
    '8': 'EIGHT ',
    '9': 'NINE '
}

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ') & (ofac_list['name'].apply(count_numbers) > 1)]

sample_size = min(500, len(ofac_list_filtered))
ofac_list_sampled = ofac_list_filtered.sample(n=sample_size)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID' , 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    name = row['name']
    test_case_name = replace_numbers(name, num_str_map)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], name, test_case_name.upper()]

final_test_cases.to_csv('final_test_cases_157.csv', index=False, columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Original Name', 'Test Case Name'])
