#DAY24
import json
json_data=[
    {'name':"RAM",'age':18,'Permanent_staff':True,'salary':75000.00,'dept_desgn':'manager'},
     {'name':"Rakesh",'age':22,'Permanent_staff':False,'salary':56000.00,'dept_desgn':"TL"},
     {'name':"Rahul",'age':24,'Permanent_staff':True,'salary':78000.00,'dept_desgn':'CEO'},
     {'name':"Rani",'age':26,'Permanent_staff':True,'salary':45000.00,'dept_desgn':'softwareEngineer'},
     {'name':"Raja",'age':28,'Permanent_staff':True,'salary':67000.00,'dept_desgn':'HR'}
res =json.dumps(json_data)
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
print(mydb)
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE JSONRECORDS1")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="jsonrecords1"
)
dbse = mydb.cursor()

dbse.execute(
    "CREATE TABLE employee (name VARCHAR(255),age INT, permanent_staff VARCHAR(255), salary DOUBLE, dept_and_designation VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for value in dbse:
    print(value)
dbse = mydb.cursor()
sql = "INSERT INTO employee (name ,age, permanent_staff,salary,dept_designation) VALUES (%s)"
value = list(
for i in res: res[i])

dbse.execute(sql, value))
