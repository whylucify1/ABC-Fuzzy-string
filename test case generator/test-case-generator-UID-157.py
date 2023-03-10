# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-157' 
theme = 'Name Part Variations'
category = 'Number Replacement'
sub_category = '> 2 numbers replaced by strings'
entity_type = 'Entity'

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
import re

# Define a function to replace numbers with strings in a given name
def replace_numbers(name):
    # Create a dictionary to map numbers to corresponding strings
    num_str_map = {'0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'}
    # Find all the numbers in the name using regular expression
    numbers = re.findall(r'\d+', name)
    # Replace each number with the corresponding string using dictionary comprehension
    for num in numbers:
        name = name.replace(num, ''.join([num_str_map[digit] for digit in num]))
    return name

# Download and filter OFAC list
ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']
ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities

# Randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n=10)
print(ofac_list_sampled)

# Create blank final test cases table
final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

# Generate test cases by replacing numbers with strings in names
for index, row in ofac_list_sampled.iterrows():
    name = row['name']
    test_case_name = replace_numbers(name)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], name, test_case_name.upper()] # append to the dataframe

print(final_test_cases)
