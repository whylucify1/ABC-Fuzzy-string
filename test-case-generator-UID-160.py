import pandas as pd

def contains_number_word(name, replacements):
    if not isinstance(name, str):
        return False
    words = name.split()
    return any(word in replacements for word in words)

def replace_strings_with_number(name, replacements):
    words = name.split()
    for i in range(len(words)):
        if words[i] in replacements:
            words[i] = replacements[words[i]]
    modified_name = ' '.join(words)
    return modified_name

uid = 'UID-160'
theme = 'Name Part Variations'
category = 'Number Replacement'
sub_category = '>2 strings replaced by number'
entity_type = 'Entity'

number_word_replacements = {
    'ONE': '1',
    'TWO': '2',
    'THREE': '3',
    'FOUR': '4',
    'FIVE': '5',
    'SIX': '6',
    'SEVEN': '7',
    'EIGHT': '8',
    'NINE': '9',
    'TEN': '10',
    'ELEVEN': '11',
    'TWELVE': '12',
    'THIRTEEN': '13',
    'FOURTEEN': '14',
    'FIFTEEN': '15',
    'SIXTEEN': '16',
    'SEVENTEEN': '17',
    'EIGHTEEN': '18',
    'NINETEEN': '19',
    'TWENTY': '20',
    'THIRTY': '30',
    'FORTY': '40',
}

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ') & (ofac_list['name'].apply(lambda x: contains_number_word(x, number_word_replacements)))]

sample_size = min(500, len(ofac_list_filtered))
ofac_list_sampled = ofac_list_filtered.sample(n=sample_size)

final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID' , 'OFAC List UID', 'Original Name', 'Test Case Name'])

for index, row in ofac_list_sampled.iterrows():
    modified_name = replace_strings_with_number(row['name'], number_word_replacements)
    final_test_name = modified_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

final_test_cases.to_csv('final_test_cases_160.csv', index=False, columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Original Name', 'Test Case Name'])
