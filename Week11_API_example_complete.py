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
    
response = requests.get(url)

pprint.pprint(response)

#%% Almost! 

pprint.pprint(response.text)

#%% Now let's work on parsing the response:
    
data = json.load(response.text)

#%% Try again!

data = json.loads(response.text)

# load vs loads:
# load() is used to read the JSON document from file and The json.
# loads() is used to convert the JSON String document into a Python dictionary

#%% Now let's practice parsing that response:

print(data['result'].keys())

#%%
print(data['result']['addressMatches'])    

#%%    
print(data['result']['addressMatches'][0])

#%%
print(data['result']['addressMatches'][0]['coordinates'])

#%%
coords = data['result']['addressMatches'][0]['coordinates']

#%%
print(coords['x'])
print(coords['y'])

#%% Now that we understand the structure of the response and how to parse it, 
# let's work on reading in a list of addresses and forming URLs so we can
# run a batch of API requests

# The easiest way to read a csv is with pandas:
adds = pd.read_csv(r'data/CO_schools.csv', encoding = 'iso-8859-1')

print(adds)

#%%
print(adds.columns)

#%%
print(adds['Sch_Name'])

#%% Iterate over rows in Pandas:
    
for index, row in adds.iterrows():
    print(row['Sch_Name'])
    
#%% Let's form a list of urls:
# First, let's break the base url into it's parts:

url_start = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address='
url_end = '&benchmark=2020&format=json'

for index,row in adds.iterrows():
    street = row['Street_Add']
    city = row['City']
    state = row['State']
    ZIP = str(row['ZIP'])
    url = url_start+street+city+state+ZIP+url_end
    print(url)

# is this right? test it... 

#%% tweak it:
for index,row in adds.iterrows():
    street = row['Street_Add']
    state = row['State']
    ZIP = str(row['ZIP'])
    url = url_start+street+' '+city+' '+state+' '+ZIP+url_end
    print(url)    

#%% Okay! HERE WE GO!

# Get the output csv ready:
newFile = open(r'results/school_coords.csv', 'w', newline='')

#%% Writer object:

writer = csv.writer(newFile)

#%% write a header row:
    
writer.writerow(['School','x','y'])

#%%
for index,row in adds.iterrows():
    name = row['Sch_Name']
    street = row['Street_Add']
    state = row['State']
    ZIP = str(row['ZIP'])
    url = url_start+street+' '+city+' '+state+' '+ZIP+url_end
    response = requests.get(url)
    data = json.loads(response.text)
    coords = data['result']['addressMatches'][0]['coordinates']
    x = coords['x']
    y = coords['y']
    writer.writerow([name,x,y])
    
newFile.close()

# CAVEATS: Census Geocoder is really slow and maybe not the best option.
# But this was just an example of doing an API request, parsing the response,
# and writing it to a file that could be imported into desktop GIS or elsewhere.