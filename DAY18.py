#DAY18
import cx_Oracle
# Create a DB with doctor and doctor ID & patients visited
con = cx_Oracle.connect('hr/hr@localhost')
cur = con.cursor()
cur.execute("Create table Doctor(doctor_id int,doctor_name varchar(20),patient_visited int)")
try:
    cur.execute("insert into Doctor values(1,'karthik',5)")
    cur.execute("insert into Doctor values(2,'kiran',6)")
    cur.execute("insert into Doctor values(4,'kamal',0)")
    cur.execute("insert into Doctor values(10,'kannan',2)")
    con.commit()
    print("Values inserted Sucessfully")
except Exception as err:
    print("Failed to insert values", err)

# Get the doctor(s) who have more than 5 patients visited
cur.execute("select * from doctor where patient_visited>5")
result = cur.fetchall()
j = 0
for i in result:
    print("Row", (j + 1), ":", i)
    j += 1
    con.commit()


# Get the doctors with no patients visit
cur.execute("select * from doctor where patient_visited=0")
re = cur.fetchall()
j = 0
for i in re:
    print("Row", (j + 1), ":", i)
    j += 1
    con.commit()


con.close()