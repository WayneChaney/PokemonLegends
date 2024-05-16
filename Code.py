__author__ = "Wayne Chaney"
__copyright__ = "Copyright 2024, The Pokemon Project"
__credits__ = ["Wayne Chaney"]
__license__ = "GPL"
__version__ = "1.0"
__pythonVersion__ = "3.12.0"
__maintainer__ = "Wayne Chaney"
__email__ = "waynechane@gmail.com"
__status__ = "Building"


import csv
import mysql.connector



with open('pokemon.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        # print(lines)
        if lines[12] == 'True':
            print(lines[1],lines[2],lines[3],lines[11])
            # print("Ledgendary")
        else:
            print("normal")




dataBase = mysql.connector.connect(
  host = "localhost",
    user = "local_user",
    password = "password",
    database = "dataBase"

)

 
# preparing a cursor object
cursorObject = dataBase.cursor()
cursorObject.execute("SHOW DATABASES")
cursorObject.execute('CREATE DATABASE IF NOT EXISTS dataBase;' )
# cursor.execute('CREATE TABLE legends (name VARCHAR(255), type VARCHAR(255), generation INTEGER(10), legendaryData VARCHAR(255))' )

  
sql = "INSERT INTO Legends (Name, Type, Generation, Legendary, PokédexNum)\
VALUES (%s, %s, %d, %s, %d)"
val = [("Nikhil", "CSE", "98", "A", "0"),
       ("Nisha", "CSE", "99", "A", "0"),
       ("Rohan", "MAE", "43", "B", "0"),
       ("Amit", "ECE", "24", "A", "0"),
       ("Anil", "MAE", "45", "B", "0"), 
       ("Megha", "ECE", "55", "A", "0"), 
       ("Sita", "CSE", "95", "A", "0")]
   
cursorObject.executemany(sql, val)
dataBase.commit()
   
# disconnecting from server
dataBase.close()



cursor = conn.cursor()
sql_query = "SELECT * FROM your_table;"
cursor.execute(sql_query)


columns = [column[0] for column in cursor.description]
data = [dict(zip(columns, row)) for row in cursor.fetchall()]

#Convert to JSON
json_data = json.dumps(data, indent=4)

# save JSON data to a file:
with open('ledgendary.json', 'w') as json_file:
    json_file.write(json_data)

# Alternatively, you can use the JSON data directly in your program:
print(json_data)