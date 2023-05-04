# Fuzzy String Matching Practicum - Agricultural Bank of China, NY

Under the U.S. Government and Department of Treasury, any U.S. citizen or entity cannot transact with any individuals, firms, or countries on the OFAC (Office of Foreign Assets Control) sanctions list. Violators will be punished financially. Therefore, if the transactions which violated the regulation were completed by one specific bank, the bank would be punished with a large fine or even a lawsuit as well. Consequently, our mission is to provide our clients with substantial test case names using fuzzy name matching and complete a classification machine learning model to prevent those violations. 

Data size: 162608 rows * 15 columns</br>
Python Packages used: H2O, PiML, numpy, pandas, and scikit learn </br>

Methodology: 
     - Created 260 test case generators </br>
     - Researched fuzzy name matching algorithms </br>
     - Performed and evaluated machine learning models </br>
     - Tuned initial classification algorithm </br>
     - Created automated reports </br>

This repository contains these items: </br>
     - **Test case generator folder:** this folder contains the 260 different test cases generator scripts, organized by UID number. </br>
     - **ABC_Code:** this is our google colaboratory code which runs the ML algorithm. </br>
     - **Sample_test_cases_with_distance.csv:** this shows our dataset with the distance metrics added. </br> 
     - **full_final_names.csv:** this is the final and complete dataset that includes 500 rows per test case generator, exact name matches, and no name matches. We used  this file to run the ML algorithm. 
