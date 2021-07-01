# DAY19
import xlrd
import cx_Oracle
try:
    loc=("STUDENT_DBS.xlsx")
    con=cx_Oracle.connect("hr/hr@localhost")
    cur=con.cursor()
    print("connected to database")

    wb = xlrd.open_workbook(loc)

    sheet = wb.sheet_by_index(0)
    print("printing bthe values of the excel database")
    for i in range(sheet.nrows):
        print(sheet.row_values(i))
    cur.execute("create table studentdatabase(SI number(5),REG number(5),NAME varchar(10),AGE float(2),GENDER varchar(2),DEPT varchar(5))")
    print("Student Database created!")
    print("Reading values from excel and adding it to the oracle database.....")
    rows=[]
    for i in range(sheet.nrows):
        temp=sheet.row_values(i)
        rows.append(temp)
    cur.executemany("insert into studentdatabase values(:1,:2,:3,:4,:5,:6)",rows)
    print("Printing values from the oracle database....")
    cur.execute("select * from studentdatabase")
    data=cur.fetchall()
    for i in data:
        for j in i:
            print(j,end=" ")
        print()
    con.commit()
    con.close()
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
