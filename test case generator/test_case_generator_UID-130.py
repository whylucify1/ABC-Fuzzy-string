# ********************
# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-130' 
theme = 'Different Name Parts'
category = 'Title'
sub_category = 'Title Difference'
entity_type = 'individual'

# ********************

def replace_title(text, titles):
    import random
    identified_title = identify_title(text)
    if identified_title:
        new_title = random.choice(titles)
        return text.replace(identified_title, new_title)
    else:
        return text

def identify_title(text):
    import re
    # Define a list of common titles
    titles = ['MR.', 'MRS.', 'MISS', 'MS.', 'DR.', 'PROF.', 'PROFESSOR', 'CAPTAIN', 
              'SERGEANT', 'MUFTI', 'HON.', 'REV.', 'CAPT.', 'SGT.', 'SIR', 'DAME', 'LADY', 
              'LORD', 'ESQ.', 'PRESIDENT', 'PRIME MINISTER', 'SENATOR', 'DUKE', 'AMBASSADOR', 'KING', 
              'QUEEN', 'PRINCE', 'PRINCESS', 'MAYOR', 'JUDGE', 'MAGISTRATE', 'MONSIEUR', 'MADAME', 
              'SENOR', 'SENORA', 'SENORITA', 'HERR', 'FRAU', 'MEVROUW', 'SIGNOR', 'SIGNORA', 
              'SHEIKH', 'IMAM', 'AYATOLLAH', 'GRAND AYATOLLAH', 'RABBI', 'CANTOR', 'CAPTAIN OF INDUSTRY', 'CHAIRMAN', 
              'CHAIRWOMAN', 'DEAN', 'ATTACHE', 'COUNSELOR', 'ENVOY', 'SECRETARY', 'CONSUL', 'NOTARY', 
              'SHERIFF', 'ARCHDEACON', 'PRIEST', 'BISHOP', 'CARDINAL', 'CHAPLAIN', 'DEACON', 'ELDER', 
              'FATHER', 'MINISTER', 'PASTOR', 'POPE', 'IMAM', 'MULLAH', 'GURU', 'SWAMI', 
              'RINPOCHE', 'LAMA', 'REBBETZIN', 'HAZZAN', 'ELDER', 'SHAMAN', 'CHIEF', 'KNIGHT', 
              'DUCHESS', 'EARL', 'COUNT', 'VISCOUNT', 'BARON', 'GOVERNOR', 'CHANCELLOR', 'CORPORAL', 
              'PRIVATE', 'ADMIRAL', 'GENERAL', 'LIEUTENANT', 'COMMANDER', 'ABBESS', 'ABBOT', 'AGHA', 
              'AESYMNETES', 'AGONOTHETES', 'AGORANOMOS', 'AIR MARSHAL', 'AKHOOND', 'ALCALDE', 'ALDERMAN', 'ALLAMAH', 
              'AMBAN', "AMIR AL-MU'MININ", 'AMPHIPOLE', 'ANAX', 'APODEKTAI', 'APOSTLE', 'ARAHANT', 'ARCHBISHOP', 
              'ARCHDUCHESS', 'ARCHDUKE', 'ARCHIATER', 'ARCHIMANDRITE', 'ARCHON', 'ARCHPRIEST', 'ARGBADH', 'ARHAT', 
              'ASAPATISH', 'ASPET', 'ASSISTANT IN VIRTUE', 'ASSISTANT PROFESSOR', 'ASSOCIATE PROFESSOR', 'ASWARAN SALAR', 'AUGUSTA', 'BAIVARAPATISH', 
              'BAPU', 'BARONESS', 'BASILEUS', 'BASILISSA', 'BUDDHA', 'BEGUM', 'CARDINAL', 'CAESAR', 
              'CALIPH', 'CATHOLICOS', 'CENTURION', 'CHAKRAVARTIN', 'CHANYU', 'CHHATRAPATI', 'CHIEFTAIN', 'CHILARCH', 
              'CHORBISHOP', 'CHOREGOS', 'CITY MANAGER', 'COIFFURE ATTENDANT', 'COLONEL', 'COMES', 'COMMISSIONER', 
              'CONCUBINUS', 'CONSORT', 'CORPORAL', 'CORRECTOR', 'COUNCILLOR', 'COUNTESS', 'DAIFU', 'DALAI LAMA', 
              'DOM', 'DATHAPATISH', 'DIAKONISSA', 'DECURIO', 'DESAI', 'DESPOT', 'DILOCHITES', 'DIKASTES', 
              'DIMOIRITES', 'DIVINE ADORATRICE', 'DIWAN', 'DON', 'DONA', 'DUX', 'EARL MARSHAL', 'EMERITUS', 
              'EMPEROR', 'EMPRESS', 'EN', 'EPHOR', 'EPIHIPPARCH', 'SQUIRE', 'ESQUIRE', 'EXARCH', 
              'FAQIH', 'FELLOW', 'FIDALGO', 'FIDEI DEFENSOR', 'FIELD MARSHAL', 'FOREIGN MINISTER', 'FUREN', 'FURST', 
              'FURSTIN', 'GANDEN TRIPA', 'GENERALISSIMO', 'GONG', 'GONG BAO', 'GOODMAN', 'GOODWIFE', 'GOTHI', 
              'GYOJA', 'GRAND ADMIRAL', 'GRAND DUCHESS', 'GRAND DUKE', 'GRAND INQUISITOR', 'GRAND MASTER', 'GRAND PRINCE', 'GUARDIAN IMMORTAL', 
              'HADRAT', 'HATY-A', 'HAZARAPATISH', 'HEADMAN', 'HEGUMEN', 'HEGUMENIA', 'HEKATONARCHES', 'HELLENOTAMIAE', 
              'HETMAN', 'HEARLD', 'HERZOG', 'HIDALGO', 'HIERODEACON', 'HIEROMONK', 'HIEROPHANT', 'HIGH PRIEST', 
              'HIGH PRIESTESS', 'HIPPARCHUS', 'HOJATOLESLAM', 'ILLARCHES', 'IMAM', 'IMPERATOR', 'IMPERATRICE', 'INQUISITOR', 
              'JAGIRDAR', 'JIAOSHOU', 'JUNIOR TECHNICIAN', 'KANSTRESIOS', 'KARO', 'KHAN', 'CHAM', 'KHAWAJA', 
              'KING OF ARMS', 'KOLAKRETAI', 'KUMAR', 'KUMARI', 'LADY OF HIS MAJESTY', 'LADY OF TREASURE', 'LAOSHI', 'LECTURER', 
              'LEGATUS', 'LEHENDAKARI', 'LOCHAGOS', 'LONKO', 'LORD GREAT CHAMBERLAIN', 'LORD PRIVY SEAL', 'LUGAL', 'MAGISTER OFFICIORUM', 
              'MAGISTER MILITUM', 'MAHA-KSHTRAPA', 'MAHARAJA', 'MAHARANI', 'MAHARANA', 'MAHARAO', 'MAHATMA', 'MAJOR ARCHBISHOP', 
              'MALIK', 'MALIKAH', 'MARZBAN', 'MASTER OF THE HORSE', 'MASTER OF THE SACRED PALACE', 'MAWLAWI', 'METROPOLITAN BISHOP', 'MIRZA', 
              'MONSIGNOR', 'MULLAH', 'NAIB', 'NAKHARAR', 'NATIONAL SECURITY ADVISOR', 'NAVARCH', 'NAWAB', 'NAWABZADA', 
              'NAWABZADI', 'NIZAM', 'NOBILISSIMUS', 'NOMARCH', 'NUNCIO', 'NUSHI', 'OPTIO', 'PALATINE', 
              'PATRIARCH', 'PATROON', 'PAYGAN SALARAPOO', 'PESHWA', 'PHARAOH', 'PIR', 'PIRANI', 'POLEMARCH', 
              'POST MASTER GENERAL', 'PRAETOR', 'PRESBYTER', 'PRIMATE', 'PRINCEPS', 'PRINCIPAL LECTURER', 'PRITHVI-VALLABHA', 'PROFESSOR EMERITUS', 
              'PROPAGATOR OF DEPORTMENT', 'PROTODEACON', 'PROXENOS', 'PRYTANEIS', 'PURSUIVANT', 'RAJA', 'RANI', 'RAJMATA', 
              'READER', 'RECTOR', 'ROJU', 'SACRISTAN', 'SAINT', 'SAKELLARIOS', 'SAHIB', 'SAHIBAH', 
              'SATRAP', 'SAVAKABUDDHA', 'SEBASTOKRATOR', 'SEBASTOS', 'SEBASTE', 'SECRETARY OF STATE', 'SELECTED LADY', 'SHAH', 
              'SHAMAN', 'SHIFU', 'SHIGONG', 'SHIMU', 'SHOFET', 'SHOGUN', 'SIBYL', 'SISTER', 
              'SOMATOPHYLAX', 'SOTER', 'SPAHBOD', 'SPARAPET', 'SRI', 'SUSHRI', 'STAROSTA', 'STRATEGOS', 
              'SUBEDAR', 'SULTAN', 'SUNIM', 'SWAMI', 'SYNTAGMATARCHIS', 'TAGMATARCHIS', 'TAITAI', 'TANUTER', 
              'TAOISEACH', 'TAXIARCH', 'TEMPLE BOY', 'TENZO', 'TETRARCH', 'THAKORE', 'THAKURANI', 'THEORODOKOI', 
              'THEOROI', 'TIRBODH', 'TONGZHI', 'TOQUI', 'TRIBUNE', 'TRIERARCH', 'TSAR', 'TSARITSA', 
              'UNSUI', 'UPASAKA', 'UPAJJHAYA', 'VAJRACHARYA', 'VARMA', 'VENERABLE', 'VICAR GENERAL', 'VICEROY', 
              'VICEREINE', 'VOIVODE', 'WEIYUAN', 'XIAOJIE', 'XIAOZHANG', 'XRY HBT', 'YISHENG', 'YISHI', 
              'YUVRAJ', 'YUVRANI', 'ZAMINDAR', 'ZONGSHI', 'ZHUXI', 'STADTHOLDER', 'STEWARD', 'STEWARDESS', 
              'PHRA MAHESI', 'PHRA SANOM', 'SOMDET CHAO FA', 'PHRA ONG CHAO', 'MOM CHAO', 'CHAO FA', 'MOM RACHAWONG', 'MOM LUANG', 
              'SOMDET KROM PHRAYA', 'SOMDET PHRA', 'KROM PHRA', 'KROMMA LUANG', 'KROMMA KHUN', 'KROMMA MUEN', 'CHAO PHRAYA', 'PHRAYA', 
              'PHRA', 'LUANG', 'KHUN', 'MEUN', 'PHAN', 'NAI', 'CHAO', 'NAYOK RATTHAMONTRI', 
              'PHU WA', 'NAYOK', 'RATTHAMONTRI']
    for title in titles:
        regex = re.compile(fr'\b{title}\b.*', re.IGNORECASE)
        if regex.search(text):
            return title
    return None

#%%
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
import random

# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate entities

titles = ['MR.', 'MRS.', 'MISS', 'MS.', 'DR.', 'PROF.', 'PROFESSOR', 'CAPTAIN', 
              'SERGEANT', 'MUFTI', 'HON.', 'REV.', 'CAPT.', 'SGT.', 'SIR', 'DAME', 'LADY', 
              'LORD', 'ESQ.', 'PRESIDENT', 'PRIME MINISTER', 'SENATOR', 'DUKE', 'AMBASSADOR', 'KING', 
              'QUEEN', 'PRINCE', 'PRINCESS', 'MAYOR', 'JUDGE', 'MAGISTRATE', 'MONSIEUR', 'MADAME', 
              'SENOR', 'SENORA', 'SENORITA', 'HERR', 'FRAU', 'MEVROUW', 'SIGNOR', 'SIGNORA', 
              'SHEIKH', 'IMAM', 'AYATOLLAH', 'GRAND AYATOLLAH', 'RABBI', 'CANTOR', 'CAPTAIN OF INDUSTRY', 'CHAIRMAN', 
              'CHAIRWOMAN', 'DEAN', 'ATTACHE', 'COUNSELOR', 'ENVOY', 'SECRETARY', 'CONSUL', 'NOTARY', 
              'SHERIFF', 'ARCHDEACON', 'PRIEST', 'BISHOP', 'CARDINAL', 'CHAPLAIN', 'DEACON', 'ELDER', 
              'FATHER', 'MINISTER', 'PASTOR', 'POPE', 'IMAM', 'MULLAH', 'GURU', 'SWAMI', 
              'RINPOCHE', 'LAMA', 'REBBETZIN', 'HAZZAN', 'ELDER', 'SHAMAN', 'CHIEF', 'KNIGHT', 
              'DUCHESS', 'EARL', 'COUNT', 'VISCOUNT', 'BARON', 'GOVERNOR', 'CHANCELLOR', 'CORPORAL', 
              'PRIVATE', 'ADMIRAL', 'GENERAL', 'LIEUTENANT', 'COMMANDER', 'ABBESS', 'ABBOT', 'AGHA', 
              'AESYMNETES', 'AGONOTHETES', 'AGORANOMOS', 'AIR MARSHAL', 'AKHOOND', 'ALCALDE', 'ALDERMAN', 'ALLAMAH', 
              'AMBAN', "AMIR AL-MU'MININ", 'AMPHIPOLE', 'ANAX', 'APODEKTAI', 'APOSTLE', 'ARAHANT', 'ARCHBISHOP', 
              'ARCHDUCHESS', 'ARCHDUKE', 'ARCHIATER', 'ARCHIMANDRITE', 'ARCHON', 'ARCHPRIEST', 'ARGBADH', 'ARHAT', 
              'ASAPATISH', 'ASPET', 'ASSISTANT IN VIRTUE', 'ASSISTANT PROFESSOR', 'ASSOCIATE PROFESSOR', 'ASWARAN SALAR', 'AUGUSTA', 'BAIVARAPATISH', 
              'BAPU', 'BARONESS', 'BASILEUS', 'BASILISSA', 'BUDDHA', 'BEGUM', 'CARDINAL', 'CAESAR', 
              'CALIPH', 'CATHOLICOS', 'CENTURION', 'CHAKRAVARTIN', 'CHANYU', 'CHHATRAPATI', 'CHIEFTAIN', 'CHILARCH', 
              'CHORBISHOP', 'CHOREGOS', 'CITY MANAGER', 'COIFFURE ATTENDANT', 'COLONEL', 'COMES', 'COMMISSIONER', 
              'CONCUBINUS', 'CONSORT', 'CORPORAL', 'CORRECTOR', 'COUNCILLOR', 'COUNTESS', 'DAIFU', 'DALAI LAMA', 
              'DOM', 'DATHAPATISH', 'DIAKONISSA', 'DECURIO', 'DESAI', 'DESPOT', 'DILOCHITES', 'DIKASTES', 
              'DIMOIRITES', 'DIVINE ADORATRICE', 'DIWAN', 'DON', 'DONA', 'DUX', 'EARL MARSHAL', 'EMERITUS', 
              'EMPEROR', 'EMPRESS', 'EN', 'EPHOR', 'EPIHIPPARCH', 'SQUIRE', 'ESQUIRE', 'EXARCH', 
              'FAQIH', 'FELLOW', 'FIDALGO', 'FIDEI DEFENSOR', 'FIELD MARSHAL', 'FOREIGN MINISTER', 'FUREN', 'FURST', 
              'FURSTIN', 'GANDEN TRIPA', 'GENERALISSIMO', 'GONG', 'GONG BAO', 'GOODMAN', 'GOODWIFE', 'GOTHI', 
              'GYOJA', 'GRAND ADMIRAL', 'GRAND DUCHESS', 'GRAND DUKE', 'GRAND INQUISITOR', 'GRAND MASTER', 'GRAND PRINCE', 'GUARDIAN IMMORTAL', 
              'HADRAT', 'HATY-A', 'HAZARAPATISH', 'HEADMAN', 'HEGUMEN', 'HEGUMENIA', 'HEKATONARCHES', 'HELLENOTAMIAE', 
              'HETMAN', 'HEARLD', 'HERZOG', 'HIDALGO', 'HIERODEACON', 'HIEROMONK', 'HIEROPHANT', 'HIGH PRIEST', 
              'HIGH PRIESTESS', 'HIPPARCHUS', 'HOJATOLESLAM', 'ILLARCHES', 'IMAM', 'IMPERATOR', 'IMPERATRICE', 'INQUISITOR', 
              'JAGIRDAR', 'JIAOSHOU', 'JUNIOR TECHNICIAN', 'KANSTRESIOS', 'KARO', 'KHAN', 'CHAM', 'KHAWAJA', 
              'KING OF ARMS', 'KOLAKRETAI', 'KUMAR', 'KUMARI', 'LADY OF HIS MAJESTY', 'LADY OF TREASURE', 'LAOSHI', 'LECTURER', 
              'LEGATUS', 'LEHENDAKARI', 'LOCHAGOS', 'LONKO', 'LORD GREAT CHAMBERLAIN', 'LORD PRIVY SEAL', 'LUGAL', 'MAGISTER OFFICIORUM', 
              'MAGISTER MILITUM', 'MAHA-KSHTRAPA', 'MAHARAJA', 'MAHARANI', 'MAHARANA', 'MAHARAO', 'MAHATMA', 'MAJOR ARCHBISHOP', 
              'MALIK', 'MALIKAH', 'MARZBAN', 'MASTER OF THE HORSE', 'MASTER OF THE SACRED PALACE', 'MAWLAWI', 'METROPOLITAN BISHOP', 'MIRZA', 
              'MONSIGNOR', 'MULLAH', 'NAIB', 'NAKHARAR', 'NATIONAL SECURITY ADVISOR', 'NAVARCH', 'NAWAB', 'NAWABZADA', 
              'NAWABZADI', 'NIZAM', 'NOBILISSIMUS', 'NOMARCH', 'NUNCIO', 'NUSHI', 'OPTIO', 'PALATINE', 
              'PATRIARCH', 'PATROON', 'PAYGAN SALARAPOO', 'PESHWA', 'PHARAOH', 'PIR', 'PIRANI', 'POLEMARCH', 
              'POST MASTER GENERAL', 'PRAETOR', 'PRESBYTER', 'PRIMATE', 'PRINCEPS', 'PRINCIPAL LECTURER', 'PRITHVI-VALLABHA', 'PROFESSOR EMERITUS', 
              'PROPAGATOR OF DEPORTMENT', 'PROTODEACON', 'PROXENOS', 'PRYTANEIS', 'PURSUIVANT', 'RAJA', 'RANI', 'RAJMATA', 
              'READER', 'RECTOR', 'ROJU', 'SACRISTAN', 'SAINT', 'SAKELLARIOS', 'SAHIB', 'SAHIBAH', 
              'SATRAP', 'SAVAKABUDDHA', 'SEBASTOKRATOR', 'SEBASTOS', 'SEBASTE', 'SECRETARY OF STATE', 'SELECTED LADY', 'SHAH', 
              'SHAMAN', 'SHIFU', 'SHIGONG', 'SHIMU', 'SHOFET', 'SHOGUN', 'SIBYL', 'SISTER', 
              'SOMATOPHYLAX', 'SOTER', 'SPAHBOD', 'SPARAPET', 'SRI', 'SUSHRI', 'STAROSTA', 'STRATEGOS', 
              'SUBEDAR', 'SULTAN', 'SUNIM', 'SWAMI', 'SYNTAGMATARCHIS', 'TAGMATARCHIS', 'TAITAI', 'TANUTER', 
              'TAOISEACH', 'TAXIARCH', 'TEMPLE BOY', 'TENZO', 'TETRARCH', 'THAKORE', 'THAKURANI', 'THEORODOKOI', 
              'THEOROI', 'TIRBODH', 'TONGZHI', 'TOQUI', 'TRIBUNE', 'TRIERARCH', 'TSAR', 'TSARITSA', 
              'UNSUI', 'UPASAKA', 'UPAJJHAYA', 'VAJRACHARYA', 'VARMA', 'VENERABLE', 'VICAR GENERAL', 'VICEROY', 
              'VICEREINE', 'VOIVODE', 'WEIYUAN', 'XIAOJIE', 'XIAOZHANG', 'XRY HBT', 'YISHENG', 'YISHI', 
              'YUVRAJ', 'YUVRANI', 'ZAMINDAR', 'ZONGSHI', 'ZHUXI', 'STADTHOLDER', 'STEWARD', 'STEWARDESS', 
              'PHRA MAHESI', 'PHRA SANOM', 'SOMDET CHAO FA', 'PHRA ONG CHAO', 'MOM CHAO', 'CHAO FA', 'MOM RACHAWONG', 'MOM LUANG', 
              'SOMDET KROM PHRAYA', 'SOMDET PHRA', 'KROM PHRA', 'KROMMA LUANG', 'KROMMA KHUN', 'KROMMA MUEN', 'CHAO PHRAYA', 'PHRAYA', 
              'PHRA', 'LUANG', 'KHUN', 'MEUN', 'PHAN', 'NAI', 'CHAO', 'NAYOK RATTHAMONTRI', 
              'PHU WA', 'NAYOK', 'RATTHAMONTRI']
#Created a filter to include all of the names that have titles in them 
title_filter = ofac_list_filtered['name'].str.split().str[0].isin(titles)

# apply the filter
filtered_df = ofac_list_filtered[title_filter]

print(filtered_df)

# randomly choose 2 rows
ofac_list_sampled = filtered_df.sample(n=2)
print(ofac_list_sampled)

# ---------------------
# CREATE THE TEST CASES
# ---------------------

# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    names = row['name'].upper()
    last_name, first_name = names.split(",")
    last_name = last_name.strip()
    first_name = first_name.strip()
    new_name = first_name + ' ' + last_name
    final_test_name = replace_title(new_name, titles)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)