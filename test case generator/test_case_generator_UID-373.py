
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-373' 
theme = 'Special Characters and Spaces'
category = 'Removal'
sub_category = '2 special characters removed'
entity_type = 'entity'

# ********************

#%%
import numpy as np
x = 2# change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages
import re
import pandas as pd


# Download the OFAC list from the web
ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


# filter for the requirements of the specific test case type
ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities

# Filter for names with exactly one special character
def has_one_special_char(name):
    special_chars = re.findall(r'[^\w\s]', name)
    return len(special_chars) == 1

ofac_list_filtered_one_special_char = ofac_list_filtered[ofac_list_filtered['name'].apply(has_one_special_char)]

# Randomly choose 500 rows or the total number of rows if there are less than 500 rows
num_rows = ofac_list_filtered_one_special_char.shape[0]
num_samples = min(500, num_rows)
ofac_list_sampled = ofac_list_filtered_one_special_char.sample(n=num_samples)

# Print the sampled DataFrame
print(ofac_list_sampled)


#####




##




def remove_special_chars(entity_name):
    # find all special characters in the entity name
    special_chars = re.findall(r'[^\w\s]', entity_name)

    # check if there are two or more special characters
        
    if len(special_chars) >= 2:

        entity_name = re.sub(r'[^\w\s]', '', entity_name, count=2)
        
    if len(special_chars) ==1:

            entity_name = re.sub(r'[^\w\s]', '', entity_name, count=1)
        

    return entity_name



#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    busdes_name = row['name']
    words = busdes_name.split()
    first_word = words[0]
    last_word = words[-1]
    middle_words = words[1:-1]
    
    special_remove_name=remove_special_chars(busdes_name)
  
    final_test_name=special_remove_name

    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]

    print(final_test_name)
    
    
    

final_test_cases[['UID','Theme','Category',	'Sub-category',	'Entity-Type',	'Original Name',	'Test Case Name']].to_csv('test_cases_373.csv', index=False, header=['UID','Theme','Category',	'Sub-category',	'Entity-Type',	'Original Name','Test Case Name'])


  
    