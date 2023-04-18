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
file = open(r'class.json', encoding = 'utf-8')



#%% use json.load() to make python read the json data as a dictionary
data = json.load(file)

#%% Explore:
print(data)

#%%
print(data.keys())

#%%
people = data['people']

print(people)

#%% Pretty print can be helpful at this stage:    
pprint.pprint(people)


#%% Try some iterating:
for person in people:
    print(person)
    print('**************')

#%%
for person in people:
    print(person['age'])


#%%
phil = people[0]

#%% print one person's keys and values:    
print(phil)
print(phil.keys())
print(phil.values())

#%% Now in a loop:
for k,v in phil.items():
    print(k,v)

#%%     
for person in people:
    for k,v in person.items():
        print(k,':',v)
    print('**************')

#%% Let's try getting each person's seat position:

for person in people:
    print (person['seatPosition'])

#%% Let's get our keys into a list:    
keys = []
for key in people[0].keys():
    keys.append(key)

#%% OR, better(?) way:
keys = list(people[0].keys())

#%% Now, let's work on parsing our json values into a CSV:
newFile = open(r'results/people2.csv', 'w', newline='')

# Note: 'w' is for write. This will overwrite whatever is there.
# Use 'a' to append, or add new lines below what is already there.
#%% instantiate the writer object:
writer = csv.writer(newFile)

#%% Write the keys to the first row, to serve as field headings:
writer.writerow(keys)

#%% Now let's parse our json and write the data into the rows of the CSV:
for person in people:
    ID = person['id']
    fn = person['firstName']
    ln = person['lastName']
    role = person['role']
    seat = person['seatPosition']
    age = person['age']
    writer.writerow([ID,fn,ln,role,seat,age])

#%% Close the file
newFile.close()