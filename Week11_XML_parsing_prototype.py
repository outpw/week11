#******************************
# Week12 Example: Parsing XML
# Created by:  Phil White
# Updated on:  04/17/2023, PW
# Description: A basic example of how to work with XML data
#******************************

#%% Imports
import xml.etree.cElementTree as et
import os
import csv

#%% Change your directory 
os.chdir(r'c:/users/phwh9568/geog_4303/week11/data')

#%% open the class.xml file



#%% use et.parse to make it into something Python understands:

    

#%% Get the root element of the xml:

    


print(root)
print(len(root))

#%% Let's examine the first element at index position 0:

    

print(person1)

#%%
print(p )

#%%
print( )

#%% get the 'firstname' element for the first item:

    

print(name)

#%% But if you want the actual data value:
    
print( )

#%% Again for all of them:

    






print(firstName, lastName, role, seat, age)

#%% How do we get everything? Loop!




#%%





# Easy right? (Well, this is an easy file to work with...)

#%% Now let's create a csv and write our xml data into a csv:

    

#%% instantiate the writer object:

    

#%% Write the first row of the csv, which in this case will be a header:

    

#%% Loop through the root and grab the data values for each element using the 
# Same methods as before. Then, write them to a new row in your csv:

    


