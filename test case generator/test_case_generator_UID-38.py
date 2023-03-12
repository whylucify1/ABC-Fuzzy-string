uid = 'UID-38' 
theme = 'Name Additions'
category = 'Middle Name'
sub_category = '2 middle name added'
entity_type = 'individual'

# ********************

#%%
def add_random_middle_name(name, middle_name_list):
        import random
        middle_name_list = ["LIAM", 'OLIVIA', 'NOAH', 'EMMA', 'OLIVER', 'CHARLOTTE', 'ELIJAH', 'AMELIA', 
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
        words = name.split(", ")
        last_name = words[0]
        first_name_middle_names = words[1]
        first_name_middle_names_parts = first_name_middle_names.split(" ")
        first_name = first_name_middle_names_parts[0]
        middle_name1 = random.choice(middle_name_list)
        middle_name2 = random.choice(middle_name_list)
        full_name_parts = [first_name] + [middle_name1] + [middle_name2] + first_name_middle_names_parts[1:]
        full_name = " ".join(full_name_parts) + " " + " " + last_name
        return full_name
#******
#%%
import numpy as np
x = 4 # change when you want different results
np.random.seed(x)
# ------------------------------------
# IMPORT DATA, PACKAGES, AND FUNCTIONS
# ------------------------------------

# import the relevant functions and packages

import pandas as pd
from test_case_generator_functions import add_random_middle_name
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
middle_name_list = ["LIAM", 'OLIVIA', 'NOAH', 'EMMA', 'OLIVER', 'CHARLOTTE', 'ELIJAH', 'AMELIA', 
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

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])

#run loop to generate the test cases 
for index, row in ofac_list_sampled.iterrows():
    names = row['name'].upper()
    final_test_name = add_random_middle_name(names, middle_name_list)
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name.upper()]
    print(final_test_name)