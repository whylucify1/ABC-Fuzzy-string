# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-19' 
theme = 'Name Additions'
category = 'First name'
sub_category = 'First name added'
entity_type = 'individual'

# ********************
def random_first_names():
    import random 
    first_name_list = ["LIAM", 'OLIVIA', 'NOAH', 'EMMA', 'OLIVER', 'CHARLOTTE', 'ELIJAH', 'AMELIA', 
                       'JAMES', 'AVA', 'WILLIAM', 'ALEXANDER', 'SOPHIA', 'ISABELLA', 'BENJAMIN', 'BEN', 
                       'ISABELLA', 'ISABELL', 'LUCAS', 'MIA', 'HENRY', 'EVELYN', 'THEODORE', 'HARPER', 
                       'DEBORAH', 'STEVEN', 'STEPHEN', 'MATTHEW', 'MATT', 'MARY', 'PATRICIA', 'ROBERT', 
                       'BOB', 'CARLA', 'JAYDEN', 'NOVA', 'AMARA', 'ELLA', 'ETHAN', 'MORGAN', 
                       'LUCA', 'ARIA', 'EMILY', 'JULIE', 'LAURA', 'LIAM', 'MEGAN', 'LEO', 
                       'JACK', 'AVERY', 'ASHER', 'THEODORE', 'AVA', 'CLAUDIA', 'ELIZABETH', 'LIZ', 
                       'ZACH', 'MIKE', 'MICHAEL', 'SARAH', 'CHLOE', 'LUNA', 'JORDAN', 'GEORGE', 
                       'RUBY', 'AMANDA', 'MIRANDA', 'JACOB', 'MELANIE', 'SHANNON', 'JULIAN', 'NICHOLAS', 
                       'NATHAN', 'ADAM', 'JAKE', 'MARIA', 'MOHAMMED', 'JOSE', 'JESUS', 'AHMED',  
                       'ALISON', 'ANNA', 'JUAN', 'KATHY', 'MARY', 'DANIEL', 'LUIS', 'CARLOS', 
                       'ANTONIO', 'JOSEPH', 'ELENA', 'LOUIS', 'JOHN', 'CHARLES', 'FRANK', 'THOMAS', 
                       'EDWARD', 'HARRY', 'WALTER', 'ARTHUR', 'FRED', 'ALBERT', 'SAMUEL', 'DAVID', 
                       'JOE', 'CHARLIE', 'CLARENCE', 'ANDREW', 'ERNEST', 'WILL', 'JESSE', 'OSCAR', 
                       'LEWIS', 'PETER', 'FREDERICK', 'TOM', 'JIM', 'LEONARD', 'HORATIO', 'CHESTER', 
                       'WARREN', 'JESSIE', 'CARL', 'ALEX', 'MARK', 'HARLEY', 'BILL', 'GORDON', 
                       'WAYNE', 'MASON', 'JASON', 'JOHNNY', 'HARDY', 'FRANCISCO', 'CLAY', 'MALCOLM', 
                       'ALEXA', 'ALLISON', 'ALYSSA', 'ADRIANA', 'ADELE', 'ZOEY', 'CAITLIN', 'CAROLINE', 
                       'CECILIA', 'BROOKLYN', 'EDEN', 'ELEANOR', 'ELISE', 'FIONA', 'GEMMA', 'GIANNA', 
                       'DONNA', 'GRETA', 'HANNAH', 'JESSICA', 'JENNA', 'JULIA', 'JULIET', 'KATE', 
                       'KATHERINE', 'KAYLEE', 'MATILDA', 'MARGARET', 'MICHAELA', 'MICHELLE', 'MINDY', 'MIRIAM', 
                       'MOLLY', 'MADELINE', 'NAOMI', 'REBECCA', 'ERICA', 'MAYA', 'PAIGE', 'NORA', 
                       'RUTH', 'RYAN', 'SABRINA', 'SADIE', 'SCARLETT', 'SKYLAR', 'SYDNEY', 'TALIA', 
                       'VANESSA', 'VERONICA', 'VIOLET', 'VIVIAN', 'ABDUL', 'ABUDLLAH', 'AHMED', 'AIDEN', 
                       'ALAN', 'ALLEN', 'ANTHONY', 'BRANDON', 'CALEB', 'BRIAN', 'CHRISTIAN', 'CHRISTOPHER', 
                       'CHRIS', 'CARSON', 'CONNOR', 'DANNY', 'DEREK', 'DYLAN', 'GABRIEL', 'IAN', 
                       'ISAAC', 'IVAN', 'JACKSON', 'GAVIN', 'KEVIN', 'JUSTIN', 'LOGAN', 'LUKE', 
                       'MARTIN', 'MAX', 'NELSON', 'OWEN', 'PETER', 'ROHAN', 'STANLEY', 'TIMOTHY', 
                       'TONY', 'TYLER', 'VICTOR', 'ZACHARY', 'XAVIER', 'CHAD', 'CHASE', 'CODY', 
                       'HUNTER', 'SHAWN', 'TAYLOR', 'ED', 'PATRICK', 'SEAN', 'SEBASTIAN', 'ANDREW', 
                       'ANTONIO', 'ARMANI', 'ASHTON', 'CHRISTY', 'CINDY', 'CLAIRE', 'CLARA', 'DAISY', 
                       'BELLA', 'FATIMA', 'GRACE', 'HAILEY', 'HELEN', 'IVY', 'JANICE', 'JASMINE', 
                       'JENNIFER', 'LILLIAN', 'LILY', 'LAUREN', 'MADISON', 'DOVE', 'ESPIE', 'DAN', 
                       'LUCY', 'MARCO', 'KAYLA', 'ALEXA', 'MELODY', 'NATALIE', 'NICOLE', 'RACHEL', 
                       'BROOKE', 'ABBY', 'KELSEY', 'LISA', 'PEDRO', 'LEX', 'DOMINIQUE', 'MARESSA']
    random_first_names = first_name_list[random.randrange(1,280)]
    return random_first_names

#%%
import numpy as np
x = 5 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import random_first_names
# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

#%%

# ------------------------------------------------------
# FILTER FOR THE REQUIREMENTS OF THE NAME VARIATION TYPE
# ------------------------------------------------------

# filter for the requirements of the specific test case type

ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate entities
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
    individual_names = row['name']
    last_name, first_name = individual_names.split(",")
    last_name = last_name.strip()
    first_name = first_name.strip()
    final_test_name = random_first_names() + ' ' + first_name + ' ' + last_name
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)
