# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-16' 
theme = 'Name Additions'
category = 'Company Location'
sub_category = '1 name part added'
entity_type = 'entity'

# ********************
def rand_location(): 
    import random 
    locations = ["AFGHANISTAN", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA",
                 "ANTIGUA AND BARBUDA", "ARGENTINA", "ARMENIA", "AUSTRALIA", "AUSTRIA", 
                 "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS",
                 "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BHUTAN", 
                 "BOLIVIA", "BOSNIA AND HERZEGOVINA", "BOTSWANA", "BRAZIL", "BRUNEI", 
                 "BULGARIA", "BURKINA FASO", "BURUNDI", "CABO VERDE", "CAMBODIA", 
                 "CAMEROON", "CANADA", "CENTRAL AFRICAN REPUBLIC", "CHAD", "CHILE", 
                 "CHINA", "COLOMBIA", "COMOROS", "DEMOCRATIC REPUBLIC OF THE CONGO", "REPUBLIC OF THE CONGO",
                 "COSTA RICA", "COTE D'IVOIRE", "CROATIA", "CUBA", "CYPRUS",
                 "CZECH REPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICAN REPUBLIC", 
                 "ECUADOR", "EGYPT", "EL SALVADOR", "EQUATORIAL GUINEA", "ERITREA", 
                 "ESTONIA", "ESWATINI", "ETHIOPIA", "FIJI", "FINLAND", 
                 "FRANCE", "GABON", "GAMBIA", "GEORGIA", "GERMANY", 
                 "GHANA", "GREECE", "GRENADA", "GUATEMALA", "GUINEA", 
                 "GUINEA-BISSAU", "GUYANA", "HAITI", "HONDURAS", "HUNGARY", 
                 "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", 
                 "IRELAND", "ISRAEL", "ITALY", "JAMAICA", "JAPAN", 
                 "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KOSOVO", 
                 "KUWAIT", "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", 
                 "LESOTHO", "LIBERIA", "LIBYA", "LIECHTENSTEIN", "LITHUANIA",
                 "LUXEMBOURG", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", 
                 "MALI", "MALTA", "MARSHALL ISLANDS", "MAURITANIA", "MAURITIUS", 
                 "MEXICO", "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", 
                 "MONTENEGRO", "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", 
                 "NAURU", "NEPAL", "NETHERLANDS", "NEW ZEALAND", "NICARAGUA", 
                 "NIGER", "NIGERIA", "NORTH KOREA", "NORTH MACEDONIA", "NORWAY", 
                 "OMAN", "PAKISTAN", "PALAU", "PANAMA", "PAPUA NEW GUINEA", 
                 "PARAGUAY", "PERU", "PHILIPPINES", "POLAND", "PORTUGAL", 
                 "QATAR", "ROMANIA", "RUSSIA", "RWANDA", "SAINT KITTS AND NEVIS", 
                 "SAINT LUCIA", "SAINT VINCENT AND THE GRENADINES", "SAMOA", "SAN MARINO", "SAO TOME AND PRINCIPE", 
                 "SAUDI ARABIA", "SENEGAL", "SERBIA", "SEYCHELLES", "SIERRA LEONE", 
                 "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOLOMON ISLANDS", "SOMALIA", 
                 "SOUTH AFRICA", "SOUTH KOREA", "SOUTH SUDAN", "SPAIN", "SRI LANKA", 
                 "SUDAN", "SURINAME", "SWEDEN", "SWITZERLAND", "SYRIA", 
                 "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TIMOR-LESTE", 
                 "TOGO", "TONGA", "TRINIDAD AND TOBAGO", "TUNISIA", "TURKEY",
                 "TURKMENISTAN", "TUVALU", "UGANDA", "UKRAINE", "UNITED ARAB EMIRATES", 
                 "UNITED KINGDOM", "UNITED STATES", "URUGUAY", "UZBEKISTAN", "VANUATU", 
                 "VATICAN CITY", "VENEZUELA", "VIETNAM", "YEMEN", "ZAMBIA", 
                 "ZIMBABWE"]
    rand_location = locations[random.randrange(1,195)]
    return rand_location

#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import rand_location
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

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    busdes_names = row['name']
    final_test_name = rand_location() + ' ' + busdes_names
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
