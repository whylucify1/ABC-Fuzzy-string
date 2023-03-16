
# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-56' 
theme = 'Name deletions'
category = 'Company Designator'
sub_category = '2 Company designator removed'
entity_type = 'Entity'

# ********************

#%%

# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------
def remove_matching_word(text, word_list):
    words = text.split()
    new_words = []
    match_count = 0
    for word in reversed(words):
        if word in word_list and match_count < 2:
            match_count += 1
        else:
            new_words.append(word)
    if match_count == 2:
        new_words.reverse()
        return " ".join(new_words)
    else:
        return text




word_list = ["Inc.","Corp.","LLC","Ltd.","Co.","PC","Ltda.","AG","GmbH","BV","SARL","SA","Pty. Ltd.","AB","KK","Oy",
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
             'JSC','SDNBHD','AG','BV','GMBH&COKGAA','SL','KG','FZ-LLC','SAU','SAPIDECV','SPK','DOO','NV','SAIC','LTDCO']



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

ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate individuals

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
for index, row in ofac_list_sampled.iterrows():
    new_names = row['name']
    final_test_name = remove_matching_word(new_names, word_list)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
