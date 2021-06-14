#DAY3
from tkinter import *        #IMPORTING ALL OPERATION
from tkinter import ttk

window=Tk()                                 #TO CREATE WINDOW
window.title("EMPLOYEE REGISTRATION FORM")  #TO DECLARE WINDOW TITLE
window.geometry("400x300")                  #TO DECLARE WINDOW SIZE
window.configure(background="WHITE")        #TO DECLARE WINDOW COLOUR     

#DECLARE FIELDS

FirstName=Label(window,text="FIRST NAME").grid(row=0,column=0)
LastName=Label(window,text="LAST NAME").grid(row=1,column=0)

FirstName1=Entry(window).grid(row=0,column=1)
LastName1=Entry(window).grid(row=1,column=1)

#***************************DECLARING FIELD GENDER************************************

var=IntVar()                         #CONVERT STRINT INTO INTEGER
Gender=Label(window,text="GENDER",justify=LEFT).grid(row=2,column=0)
Radiobutton(window,text="male",padx=20,variable=var,value=1).grid(row=2,column=1)
Radiobutton(window,text="female",padx=20,variable=var,value=2).grid(row=2,column=2)
Radiobutton(window,text="others",padx=20,variable=var,value=3).grid(row=2,column=3)



#*****************DECLARING FIELD DOB USING(SPINBOX)****************************************************

DOB=Label(window,text="DOB").grid(row=6,column=0)
w=Spinbox(window,from_=1,to=31)
w.grid(row=6,column=1)
w1=Spinbox(window,from_=1,to=12)
w1.grid(row=6,column=2)
w2=Spinbox(window,from_=1980,to=2010)
w2.grid(row=6,column=3)


#************************DECLARING FIELD BLOOD GROUP USING (RADIO BUTTON)************************************************


BloodGroup=Label(window,text="BLOOD GROUP",justify=LEFT).grid(row=7,column=0)
Radiobutton(window,text="0",padx=20,variable=var,value=1).grid(row=7,column=1)
Radiobutton(window,text="A",padx=20,variable=var,value=2).grid(row=7,column=2)
Radiobutton(window,text="B",padx=20,variable=var,value=3).grid(row=7,column=3)


#****************************DECLARING FIELD ID***********************************************************************
def show():
         Label.config(text=clicked.get())
         
ID=Label(window,text="ID").grid(row=11,column=0)
options=[1,2,3,4,5,6,7,8,9,10]
clicked=IntVar()
drop=OptionMenu(window,clicked,*options)
drop.grid(row=11,column=1)


#************************DECLARING FIELD CONTACT NUMBER***************************************************************************

ContactNumber=Label(window,text="CONTACT NUMBER").grid(row=12,column=0)
ContactNumber1=Entry (window).grid(row=12,column=1)

#*************************************DECLARING FIELD MAIL ID**********************************************************************

MailID=Label(window,text="MailID").grid(row=13,column=0)
MailID1=Entry(window).grid(row=13,column=1)


#**************************************DECLARING FIELD  POSITION*********************************************************

Position=Label(window,text="POSITION",justify=LEFT).grid(row=14,column=0)
Radiobutton(window,text="HR",padx=20,variable=var,value=1).grid(row=14,column=1)
Radiobutton(window,text="TEAM LEADER",padx=20,variable=var,value=2).grid(row=14,column=2)
Radiobutton(window,text="MANAGER",padx=20,variable=var,value=3).grid(row=14,column=3)

#****************************************DECLARING FIELD SALARY****************************************************************
Salary=Label(window,text="SALARY").grid(row=15,column=0)
Salary1=Entry(window).grid(row=15,column=1)


#***********************BUTTON**********************************************

def callback():
    print("welcome")

b=Button(window,text="submit",command=callback).grid(row=16,column=1)
mainloop()
