
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-34' 
theme = 'Name Additions'
category = 'Last Name Part'
sub_category = '2 Name Parts added'
entity_type = 'Entity'

# ********************



cp_last_name_list = ['Tech','Solutions','Group','International','Global','Systems','Inc.','Co.','Corp.','LLC','Enterprises','Innovations','Digital','Technologies','Services','Communications','Software','Consulting','Management','Partners','Development','Creative','Marketing','Media','Design','Labs','Ventures','Strategy','Analytics','Network','Security','Solutions','Energy','Health','Pharma','Capital','Research','Construction','Hospitality','Logistics','Manufacturing','Retail','Transportation','Financial','Investment','Insurance','Real Estate','Legal','Education','Consulting','Innovate','Dynamics','Synergy','Progress','Express','Connect','Peak','Max','Elite','Nexus','Horizon','Apex','Velocity','Quest','Summit','Blaze','Spark','Fusion','Spectrum','Evolution','Insight','Mastery','Empower','Elevate','Propel','Pioneer','Innovate','Impact','Catalyst','Sparkle','Enrich','Collaborate','Refresh','Envision','Flourish','Kinetic','Embrace','Forte','Resonate','Enrich','Vision','Radiant','Vital','Vitality','Vigor','Vitality','Rhythm','Synergy','Momentum','Harmony']


#%%

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

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

# run loop to generate the test cases
import random
for index, row in ofac_list_sampled.iterrows():
    names = row['name']
    words = names.split()
    matching_words1 = random.choice(cp_last_name_list)
    matching_words2 = random.choice(cp_last_name_list)
    words.insert(-1, str(matching_words1).upper())
    words.insert(-2, str(matching_words2).upper())
    new_company_name = ' '.join(words)
    final_test_name = new_company_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
