
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-37' 
theme = 'Name Additions'
category = 'Middle Name'
sub_category = '1 Middle Name added twice'
entity_type = 'individual'

# ********************

#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import separate_words_in_name_2, separate_words_in_name_3
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------


# Filter for individuals
ofac_list_filtered = ofac_list[ofac_list.entity_type == 'individual']

# Filter for names with a middle name
def has_middle_name(name):
    last_name, first_and_middle_names = name.split(', ', 1)
    first_and_middle_name_parts = first_and_middle_names.split()
    return len(first_and_middle_name_parts) > 2

ofac_list_filtered_middle_name = ofac_list_filtered[ofac_list_filtered['name'].apply(has_middle_name)]

# Randomly choose 500 rows or the total number of rows if there are less than 500 rows
num_rows = ofac_list_filtered_middle_name.shape[0]
num_samples = min(500, num_rows)
ofac_list_sampled = ofac_list_filtered_middle_name.sample(n=num_samples)

# Print the sampled DataFrame
print(ofac_list_sampled)




#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 



for index, row in ofac_list_sampled.iterrows():
    
    
   
    # determine for each name the number of words
    number_of_words = row['name'].count(' ') + 1 
    
    # determine for each name the number of last name words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 
    
    # determine for each name the number of first and middle name words
    
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 
    
    
    
    
    if number_of_words_first_middle > 1:
        
        # separate the name into distinct words
        separated_words = separate_words_in_name_3(row['name']) 
        
        
        
        #separate_words_in_name_3
        
        
        #abbreviated_first_name = separated_words[0]
        
        final_test_name = separated_words[0] + ' ' + separated_words[1] + ' ' + separated_words[1] + ' ' + separated_words[2]  #create the test case      
        
        # append to the dataframe
        
        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' 
                                                       + str(index), row['uid'], row['name'], final_test_name.upper()] 
        
        print(final_test_name)
        
    else: 
        separated_words = separate_words_in_name_2(row['name']) # separate the name into distinct words
        abbreviated_first_name = separated_words[0][0]
        final_test_name = separated_words[0] + '.' + ' ' + separated_words[1]  #create the test case        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' +
                                                       str(index), row['uid'], row['name'], final_test_name.upper()] # append to the dataframe
        print(final_test_name)







final_test_cases[['Sub-category', 'Original Name', 'Test Case Name']].to_csv('test_cases_37.csv', index=False, header=['Test Type', 'Original Name', 'Altered Name'])



