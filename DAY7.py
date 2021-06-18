#DAY7

#1. Create a function getting two integer inputs from user.& print the following:

#               A) Addition of two numbers is +value

#               B)Subtraction of two numbers is +value

#               C)Division of two numbers is +value

#               D)Multiplication of two numbers is +value

#Here the value represents math function associated



def getvalue():
    a=int(input("ENTER THE FIRST NUMBER:"))
    b=int(input("ENTER THE SECOND NUMBER:"))
    print("Addition of two numbers is ",add(a,b))#function call
    print("Subtraction of two numbers is ",sub(a,b))
    print("Division of two numbers is ",div(a,b))
    print("Multiplication of two numbers is ",mul(a,b))


def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def div(a,b):
    return(a/b)
def mul(a,b):
    return(a*b)
print("************Function getting two integer inputs from user & print the following*************")
getvalue()


#*********************************************************************************************************************************************************************



#2.Create a function covid( )& it should accept patient name, and body temperature, by default the body temperature should be 98 degree


def printdetails(x,y):#printing details
    print("Patient name:",x)
    print("Patient temperature:",y)
    
    
def covid(name,temperature=98):#covid() function
    patientname=name
    finaltemp=temperature
    printdetails(patientname,finaltemp)

covid("raj",99)
covid("ram")

