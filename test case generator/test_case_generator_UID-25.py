uid = 'UID-25' 
theme = 'MName Additions'
category = 'Last Name'
sub_category = '>2 Last Names added'
entity_type = 'individual'

# ********************

last_name_list = ['Smith','Johnson','Brown','Lee','Kim','Park','Choi','Kimura','Yamamoto','Hernandez','Martinez','Perez','Rodriguez','Garcia','Gonzalez','Perez','Fernandez','Silva','Santos','Oliveira','Rossi','Fischer','Mueller','Weber','Schmidt','Meier','Wagner','Becker','Schmitz','Richter','Kowalski','Nowak','Novak','Jansen','van der Meer','van der Berg','van den Broek','van der Veen','Andersen','Nielsen','Petersen','Johansson','Lindberg','Gustafsson','Jansson','Eriksson','Laine','Lehtonen','Ivanov','Petrov','Popov','Kuznetsov','Smirnov','Novikov','Sato','Tanaka','Watanabe','Nakamura','Kimura','Ono','Chen','Zhang','Li','Wang','Huang','Ng','Tan','Goh','Lim','Koh','Soh','Chong','Wong','Ng','Tan','Loh','Lee','Chang','Nguyen','Tran','Le','Vo','Nguyen','Le','Trinh','Luu','Bui','Pham','Ha','Truong','Kwon','Kim','Park','Song','Jeong','Shin','Kang','Lee','Choi','Hong']



#%%
import numpy as np
x = 7 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import random
import pandas as pd
from test_case_generator_functions import separate_words_in_name_2
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate individuals

# randomly choose 10 rows
ofac_list_sampled = ofac_list_filtered.sample(n = 10)
print(ofac_list_sampled)

#%%

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 

for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    number_of_words_last = row['name'][:row['name'].find(', ')].strip().count(' ') + 1 # determine for each name the number of last name words
    number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    if number_of_words !=1 : 
        separated_words = separate_words_in_name_2(row['name'])
        last_name_add1 = random.choice(last_name_list)
        last_name_add2 = random.choice(last_name_list)
        last_name_add3 = random.choice(last_name_list)
        final_test_name = separated_words[0] + " " + separated_words[1] +" " + last_name_add1 +" " + last_name_add2 +" " + last_name_add3  
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
        print(final_test_name)
    
