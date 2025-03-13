import sqlite3

connection = sqlite3.connect('example.db') #connect to the db

cursor = connection.cursor() # cursor object # we execuet any command on the cursor object #incharge of all the communication to the db


# Create table
cursor.execute("create table example (year integer text, name , city text)")

release_list = [(1997, "A", "rfuefhi"),
                (1999, "B", "fuefhi"),
                (2001, "C", "uefhi"),  
                (2002, "D", "efhi"),
                (2004, "E", "fhi"),
                (2008, "F", "hi"),
                (2013, "G", "i")
]

#fillin the table with data
cursor.executemany("insert into example values(?,?,?)", release_list)  


#print rows of our database

for row in cursor.execute("select * from example"):
    print(row)

#print specific rows
print("***************************************")
cursor.execute("select * from example where city=:c", {"c":"fhi"})
example_search = cursor.fetchall()
print(example_search)



#combine multiple tables and manipulate their data with python and sqlite3
#lets create a city table

cursor.execute("create table cities (example_city text, country text)")
cursor.execute("insert into cities values (?,?)", ('rfuefhi', 'efhi'))
cursor.execute("select * from cities where example_city=:c", {"c":"fhi"})
cities_search = cursor.fetchall()
print(cities_search)



#manipulate the db
print("***************************************")
for i in example_search:
    ["jdfjdbv" if value == "fhi" else value for value in i]
    print(i)
connection.close() #close the connection