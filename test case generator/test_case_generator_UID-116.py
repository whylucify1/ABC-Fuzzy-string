
# ********************
# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-116'
theme = 'Different Name Parts'
category = 'Company designator'
sub_category = '2 Company Designator difference'
entity_type = 'Entity'

# ********************

import random


def replace_designator(full_name, matching_word):
    name_parts = full_name.split()
    matching_word_count = 0
    matching_indices = []
    for i, part in enumerate(name_parts):
        if part in matching_word:
            matching_word_count += 1
            matching_indices.append(i)
    if matching_word_count == 2:
        new_word_1 = random.choice(matching_word)
        new_word_2 = random.choice(matching_word)
        while new_word_2 == new_word_1:  # To ensure that both words are different
            new_word_2 = random.choice(matching_word)
        name_parts[matching_indices[0]] = new_word_1
        name_parts[matching_indices[1]] = new_word_2
    return ' '.join(name_parts)


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


matching_word  = ["Inc.","Corp.","LLC","Ltd.","Co.","PC","Ltda.","AG","GmbH","BV","SARL","SA","Pty. Ltd.","AB","KK","Oy",
             "A/S","S.A.S.","S.A.","SRL","Sp. z o.o.","Kft.","Zrt.","GmbH & Co. KG","PLC","P.C.","Pte. Ltd.","L.P.","LLP",
             "Bhd.","NV","CV","EEIG","SE","ApS","JSC","Sdn. Bhd.","A.G.","B.V.","GmbH & Co. KGaA","S.L.","KG","FZ-LLC",
             "S.A.U.","S.A.P.I. de C.V.","Sp. k.","d.o.o.","N.V.","S.A.I.C.","Ltd. Co.",'Corporation','Company',
             'Incorporated','Limited','Co.','& Company','Associates','Group','Partners','Enterprises','LLC','Holdings',
             'International','Systems','Services','Technologies','Solutions','Inc.','Holdings','Ventures','Enterprises',
             'Corporation','Group','Associates','Global','Partners','Management','Development','Trading','Investment',
             'Holdings','Worldwide','Energy','Resources','Communications','Innovations','Industries','Logistics',
             'Distribution','Solutions','Products','Brands','Entertainment','Marketing','Media','Communications',
             'Consulting','Design','Manufacturing','Realty',"INC.","CORP.",'CORP',"LLC","LTD.","CO.","PC","LTDA.","AG",
             "GMBH","BV","SARL","SA","PTY. LTD.","AB","KK","OY","A/S","S.A.S.","S.A.","SRL","SP. Z O.O.","KFT.",
             "ZRT.","GMBH & CO. KG","PLC","P.C.","PTE. LTD.","L.P.","LLP","BHD.","NV","CV","EEIG","SE","APS","JSC",
             "SDN. BHD.","A.G.","B.V.","GMBH & CO. KGAA","S.L.","KG","FZ-LLC","S.A.U.","S.A.P.I. DE C.V.","SP. K.",
             "D.O.O.","N.V.","S.A.I.C.","LTD. CO.",'CORPORATION','COMPANY','INCORPORATED','LIMITED','CO.','& COMPANY',
             'ASSOCIATES','GROUP','PARTNERS','ENTERPRISES','LLC','HOLDINGS','INTERNATIONAL','SYSTEMS','SERVICES',
             'TECHNOLOGIES','SOLUTIONS','INC.','HOLDINGS','VENTURES','ENTERPRISES','CORPORATION','GROUP','ASSOCIATES',
             'GLOBAL','PARTNERS','MANAGEMENT','DEVELOPMENT','TRADING','INVESTMENT','HOLDINGS','WORLDWIDE','ENERGY',
             'RESOURCES','COMMUNICATIONS','INNOVATIONS','INDUSTRIES','LOGISTICS','DISTRIBUTION','SOLUTIONS','PRODUCTS',
             'BRANDS','ENTERTAINMENT','MARKETING','MEDIA','COMMUNICATIONS','CONSULTING','DESIGN','MANUFACTURING','REALTY',
             'Inc','Corp','LLC','Ltd','Co','PC','Ltda','AG','GmbH','BV','SARL','SA','PtyLtd','AB','KK','Oy','A/S','SAS',
             'SA','SRL','Spzoo','Kft','Zrt','GmbH&CoKG','PLC','PC','PteLtd','LP','LLP','Bhd','NV','CV','EEIG','SE','ApS',
             'JSC','SdnBhd','AG','BV','GmbH&CoKGaA','SL','KG','FZ-LLC','SAU','SAPIdeCV','Spk','doo','NV','SAIC','LtdCo',
             'INC','CORP','LLC','LTD','CO','PC','LTDA','AG','GMBH','BV','SARL','SA','PTYLTD','AB','KK','OY','A/S','SAS',
             'SA','SRL','SPZOO','KFT','ZRT','GMBH&COKG','PLC','PC','PTELTD','LP','LLP','BHD','NV','CV','EEIG','SE','APS',
             'JSC','SDNBHD','AG','BV','GMBH&COKGAA','SL','KG','FZ-LLC','SAU','SAPIDECV','SPK','DOO','NV','SAIC','LTDCO','OOO','OAO']

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
    names = row['name']
    final_test_name = replace_designator(names, matching_word)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)

