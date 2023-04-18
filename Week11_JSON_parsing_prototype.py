#******************************
# Week13 Example: Parsing JSON
# Created by:  Phil White
# Updated on:  04/17/2023, PW
# Description: A basic example of how to work with JSON data
#******************************
#%% Imports
import json
import csv
import os
import pprint #pretty print: conda install -c conda-forge pprintpp

#%% change directory to week 13:
os.chdir(r'c:/users/phwh9568/geog_4303/week11/data')

#%% Open class.json




#%% use json.load() to make python read the json data as a dictionary



#%% Explore:
    
print(data)

#%%
print( )

#%%


print(people)

#%% Pretty print can be helpful at this stage:    

    



#%% Try some iterating:

    


#%%




#%%



#%% print one person's keys and values:    
print( )
print( )
print( )

#%% Now in a loop:

    

#%%     




#%% Let's try getting each person's seat position:





#%% Let's get our keys into a list:    

    


#%% OR, better(?) way:

    

#%% Now, let's work on parsing our json values into a CSV:

    

# Note: 'w' is for write. This will overwrite whatever is there.
# Use 'a' to append, or add new lines below what is already there.
#%% instantiate the writer object:

    

#%% Write the keys to the first row, to serve as field headings:

    

#%% Now let's parse our json and write the data into the rows of the CSV:

    









#%% Close the file
newFile.close()