#  DAY20
import cx_Oracle
con = cx_Oracle.connect("hr/hr@localhost")
cur=con.cursor()
print("connected to database successfully")


 #   Create an Employee Table with employee name,employee ID & Salary

cur.execute("create table employee(id number(3),name varchar(10),salary float(10))")
print("table created successfully")
cur.execute("insert  into employee values(001,'kiran',65000) ")
cur.execute("insert  into employee values(002,'karan',60000)")
cur.execute("insert into employee values(003,'sugan',55000)")
cur.execute("select * from employee")



# a. Write a query to get the maximum and minimum salary from employees table
print(" ")
print("Query to get the maximum and minimum salary from employees table ")
cur.execute("select max(salary) result from employee")
print("maximum salary:", cur.fetchall()[0][0])

cur.execute("select min(salary) result from employee")
print("miniimum salary:", cur.fetchall()[0][0])

# b. Write a query to get the number of employees working with the company
print(" ")
print("********** Number of employees working with the company**************")
cur.execute("select name from employee")
n1 = cur.fetchall()
for i in n1:
    print(i)
print("number of employees working:", len(n1))

#c.Write a query to get the first 3 characters of first name from employees table
print(" ")
print("************ First 3 characters of first name from employees table*************")
cur.execute("select substr(name,1,3) from employee")
n2 =cur.fetchall()
for j in n2:
    print(j)
con.commit















