

# ********************

# ------------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# ------------------------------------

uid = 'UID-122' 
theme = 'Different Name Parts'
category = 'Middle Name'
sub_category = '1 Middle Name difference'
entity_type = 'individual'

# ********************

#%%
import numpy as np
x = 5# change when you want different results
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

import random





def modify_middle_name(middle_name):
    """
    Modifies the middle name by either adding or removing letters.

    Parameters:
    name (str): The name to modify.

    Returns:
    str: The modified name.
    """

    length = len(middle_name)
    modify_type = random.choice(["add", "remove"])
    if modify_type == "add":
        add_index = random.randint(0, length)
        add_letter = chr(random.randint(97, 122)) # Random lowercase letter
        modified_middle_name = middle_name[:add_index] + add_letter + middle_name[add_index:]
    else:
        remove_index = random.randint(0, length-1)
        modified_middle_name = middle_name[:remove_index] + middle_name[remove_index+1:]

    return modified_middle_name



def modify_middle_name(middle_name_list):
    """
    Modifies the middle name by selecting a random middle name from the list.

    Parameters:
    middle_name_list (list): The list of middle names to choose from.

    Returns:
    str: The randomly chosen middle name.
    """

    return random.choice(middle_name_list)



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


# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])



def replace_middle_name(name):
    last_name, first_and_middle_names = name.split(', ', 1)
    first_and_middle_name_parts = first_and_middle_names.split()
    if len(first_and_middle_name_parts) > 2:
        middle_name = first_and_middle_name_parts[1]
        replace=random.choice(middle_name_list)
        
        modified_name = first_and_middle_names.replace(middle_name, replace)
        return modified_name+' '+last_name+'.'
    else:
        return name




# Modify the test case generation loop
for index, row in ofac_list_sampled.iterrows():
    #number_of_words_first_middle = row['name'][row['name'].find(', ') + 1:].strip().count(' ') + 1 # determine for each name the number of first and middle name words
    
    new_name = replace_middle_name(row['name'])
   # print(new_name)
    
    modified_name=new_name
        
        
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], modified_name.upper()] # append to the dataframe
    print(modified_name)
       
   

final_test_cases[['Sub-category', 'Original Name', 'Test Case Name']].to_csv('test_cases_1225.csv', index=False, header=['Test Type', 'Original Name', 'Altered Name'])

