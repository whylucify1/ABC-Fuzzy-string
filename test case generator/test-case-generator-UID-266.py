import pandas as pd

# Set test case parameters
uid = 'UID-266'
theme = 'Names where Name Parts are Modified'
category = 'Truncation'
sub_category = '3 Letter Truncation in the end'
entity_type = 'Entity'

# Import OFAC list
ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

# Filter for entities
ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')]

# Randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n=10)
print(ofac_list_sampled)
# Create blank final test cases table
final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID', 'OFAC List UID', 'Original Name','Test Case Name'])

# Loop over each row in the sampled data
for index, row in ofac_list_sampled.iterrows():
    # Truncate the last 3 letters of the name
    truncated_name = row['name'][:-3]
    # Construct the test case name
    final_test_name = truncated_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
