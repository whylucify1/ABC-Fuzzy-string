import pandas as pd

# Set test case parameters
uid = 'UID-241'
theme = 'Names where Name Parts are Modified'
category = 'Repetitions'
sub_category = 'Very Short Name'
entity_type = 'Entity'

# Import OFAC list
ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']
#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

# Filter for entities
ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')]

# Select entities with very short names (<= 5 characters)
ofac_list_short_names = ofac_list_filtered[ofac_list_filtered['name'].str.len() <= 5]

# Create blank final test cases table
final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID', 'OFAC List UID', 'Original Name','Test Case Name'])
#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

# Loop over each row in the filtered data
for index, row in ofac_list_short_names.iterrows():
    # Check if the name has repeating characters
    repeating_chars = [char for char in row['name'] if row['name'].count(char) > 1]
    if len(repeating_chars) > 0:
        # If the name has repeating characters, replace the last repeated character with "II"
        modified_name = row['name'][0:-1] + "II" if row['name'][-1] in repeating_chars else row['name']
        # Construct the test case name
        final_test_name = modified_name.upper()
        # Append the test case to the final test cases dataframe
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + '-' + str(index), row['uid'], row['name'], final_test_name]

print(final_test_cases)
