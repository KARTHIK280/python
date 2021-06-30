# DAY17
import cx_Oracle
# 1. Create a multiple tables & insert data in table
con = cx_Oracle.connect('hr/hr@localhost')
print(con.version)
cur = con.cursor()
cur.execute("create table employee (emp_name varchar(20),position varchar2(50))")
cur.execute("create table dealers (Name varchar(20),address varchar(300),phone int)")
cur.execute("create table producer (Producername varchar(30),Details varchar(20),price float)")
try:
    ins = "insert into employee values('balaji','sales')"
    ins1 = "insert into dealer values('ganesh medi','mumbai north 2nd street',95451231)"
    ins2 = "insert into producer values('Sun pharma','covishield',840)"
    cur.execute(ins1)
    cur.execute(ins2)
    cur.execute(ins)
    print("Value inserted")
    con.commit()
except Exception as err:
    print("Failed to insert", err)

# 2. Create a employee table and read all the employee name in the table using for loop
cur.execute("select * from employee")
row = cur.fetchall()
j = 0
for i in row:
    print("Rows:", (j+1), ":", i)
    j += 1
