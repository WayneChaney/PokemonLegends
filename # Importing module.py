# Importing module 
import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "local_user",
    password = "password",
    database = "mydb"
)
 
# Printing the connection object 
print(mydb)

cursor = mydb.cursor()
 
# Creating a database with a name
# 'geeksforgeeks' execute() method 
# is used to compile a SQL statement
# below statement is used to create 
# the 'geeksforgeeks' database
#cursor.execute('CREATE DATABASE IF NOT EXISTS mydb;' )
#cursor.execute('CREATE TABLE legends (name VARCHAR(255), type VARCHAR(255), generation INTEGER(10), legendaryData VARCHAR(255))' )
#cursor.execute("SHOW DATABASES")
#Volcanion Fire Water 6
#cursor.execute('INSERT INTO legends (name, type, generation, legendaryData ) VALUES ('Volcanion','Fire','14','German');   
cursor.execute("SHOW TABLES")
sql = "INSERT INTO legends (Name, Type, Generation, Legendary, PokédexNum)\
VALUES (%s, %s, %d, %s, %d)"
val = [("Volcanion", "Fire", "14", "German", "0"),]
   
cursor.executemany(sql, val)
 
for x in cursor:
  print(x)
 
# for x in cursor:
#   print(x)