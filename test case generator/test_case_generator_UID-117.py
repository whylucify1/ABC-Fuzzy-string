
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-117' 
theme = 'Different Name Parts'
category = 'Company Location'
sub_category = '1 name part difference'
entity_type = 'entity'

# ********************

#%%
import numpy as np
x = 28 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']



#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

import random
import re

def change_country_names(text):
    # Read the list of countries
    with open('countries.txt') as f:
        countries = [country.strip() for country in f.readlines()]

    # Find all occurrences of country names in the text
    for country in countries:
        # Create a regular expression that matches the country name surrounded by word boundaries
        pattern = r'\b{}\b'.format(re.escape(country))

        # Find all occurrences of the country name in the text
        matches = re.findall(pattern, text, flags=re.IGNORECASE)

        # Replace each occurrence of the country name with a random country name
        for match in matches:
            # Choose a random country name
            new_country = random.choice(countries)

            # Replace the matched country name with the new country name
            text = text.replace(match, new_country)

    return text


final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    text = row['name']
    modified_name = change_country_names(text)
    final_test_name = modified_name.upper()
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)