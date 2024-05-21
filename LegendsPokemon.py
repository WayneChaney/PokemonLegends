__author__ = "Wayne Chaney"
__copyright__ = "Copyright 2024, The Pokemon Project"
__credits__ = ["Wayne Chaney"]
__license__ = "GPL"
__version__ = "1.0"
__pythonVersion__ = "3.12.0"
__maintainer__ = "Wayne Chaney"
__email__ = "waynechane@gmail.com"
__status__ = "Building"
#read file✔
#send type name Gen and legendary info✔\ 
#using a get, gather all pokemon legendary and write to json file

# Import module 
import csv
import json
import sqlite3 
from os import path

# Connecting to sqlite 
conn = sqlite3.connect('Legends.db') 

#creating Cursor
cursor = conn.cursor() 

# # Creating table 
table =""" CREATE TABLE IF NOT EXISTS DB(NAME VARCHAR(255), TYPE VARCHAR(255), 
TYPE2 VARCHAR(255), GEN INTEGER(10), Status VARCHAR(255));"""
cursor.execute(table) 

#Opening File and Reading
with open('pokemon.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  
  for lines in csvFile:
    #Sending Name, Type Generation and if Status of Legend
    if lines[12] == 'True':
            Qur= '''INSERT INTO DB (NAME, TYPE, TYPE2, GEN, Status) 
                  VALUES (?, ?, ?, ?, ?)'''
            
            val = (str(lines[1]),str(lines[2]),str(lines[3]),str(lines[11]), "Ledgendary")
            cursor.execute(Qur, val)

            ##print(lines[1],lines[2],lines[3],lines[11], "Ledgendary")
            
           
    else:
            print("")
            #print(lines[1],lines[2],lines[3],lines[11], "Normal")






print("===============================================================================================")
print(" ALL THE LEGENDARY POKEMON IN THE DATA BASE")
print("===============================================================================================")


data=cursor.execute('''SELECT * FROM DB''') 
for row in data: 
    print(row)




#CREATING LEGENDS OBJ
Legends= []


   
    #SELECT FROM ENTIRE DB
data=cursor.execute('''SELECT * FROM DB''') 
for row in data: 
    for column in row: 
      #GATHER LEGENDARY POKE
      if column == 'Ledgendary':
         #print(row[3])
         dictionary = { "Name": row[0],"Type": row[1],"Type2": row[2],"Gen": row[3], "Status": row[4],} 
      #ADD TO LEGEND OBJ
         Legends.append(dictionary)
         
       
       
#Write Everything to json files 
# Serializing json
json_object = json.dumps(Legends, indent=4)


# Writing to sample.json
with open("data.json", mode="w") as outfile:
    outfile.write(json_object)

# Opening JSON file
with open('data.json', mode='r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
print(type(json_object)) 
print(json_object)

print("I WANT TO BE THE VERY BEST, LIKE NO ONE EVER WAS!!!!!!!")       
 
# # # Commit your changes in 
# # # the database	 
conn.commit() 

# # # Closing the connection 
conn.close()
