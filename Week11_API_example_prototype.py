#******************************
# Week13 Example: Calling a REST API and parsing response
# Created by:  Phil White
# Updated on:  04/15/2022, PW
# Description: 
# A basic example of how to GET data from a REST API
# In this example, we query the US Census geocoder to 
# get coordinates for a list of addresses
#******************************

#%% Imports
import os
import json
import csv
import requests
import pprint
import pandas as pd

#%%
os.chdir(r'c:/users/phwh9568/geog_4303/week11/data')

#%% Calling an API:

#%% First, know the URL you want to "call":

url = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=4600+Silver+Hill+Rd%2C+Washington%2C+DC+20233&benchmark=2020&format=json'

#%% Now, we'll use requests to get the response at that URL:
    





#%% Almost! 

pprint.pprint( )

#%% Now let's work on parsing the response:
    



#%% Try again!




# load vs loads:
# load() is used to read the JSON document from file and The json.
# loads() is used to convert the JSON String document into a Python dictionary

#%% Now let's practice parsing that response:

print(  )

#%%
print( )    

#%%    
print( )

#%%
print( )

#%%
coords = 

#%%
print( )
print( )

#%% Now that we understand the structure of the response and how to parse it, 
# let's work on reading in a list of addresses and forming URLs so we can
# run a batch of API requests

# The easiest way to read a csv is with pandas:



print( )

#%%
print( )

#%%
print( )

#%% Iterate over rows in Pandas:
    


    
#%% Let's form a list of urls:
# First, let's break the base url into it's parts:

url_start = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address='
url_end = '&benchmark=2020&format=json'







# is this right? test it... 

#%% tweak it:

    




#%% Okay! HERE WE GO!

# Get the output csv ready:
newFile = open(r'results/school_coords.csv', 'w', newline='')

#%% Writer object:




#%% write a header row:
    



#%%
for index,row in adds.iterrows():

    






    
newFile.close()

# CAVEATS: Census Geocoder is really slow and maybe not the best option.
# But this was just an example of doing an API request, parsing the response,
# and writing it to a file that could be imported into desktop GIS or elsewhere.