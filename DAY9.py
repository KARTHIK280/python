#DAY9

# 1. Write a program to loop through a list of numbers and add +2 to every value to elements in list:
print("******************  Add +2 to every value to elements in list   *********************")
a=[1,3,5,6]
for i in range(0,len(a)):
    a[i] += 2
print(a)



#*******************************************************************************************************************************
# 2. Write a program to get the below pattern
#54321
#4321
#321
#21
#1

print(" ")
print("**************** Write a program to get the pattern ***************** ")
n = 5
for i in range(n): 
	print(''.join(map(str,range(n-i,0,-1)))) 


#***********************************************************************************************************************************

# 3. Python Program to Print the Fibonacci sequence:

print(" ")
print("***************** Fibonacci sequence *************** ")


a = 0
b = 1
nums=int(input("ENTER A NUMBER: "))

if nums == 1:
    print(a)
elif nums == 2:
    print(a)
    print(b)
elif nums <= 0:
    print("ENTER A VALID NUMBER:")
else:  
 for i in range(2,nums):
         c = a+b
         print(c)
         a = b
         b = c
         
#******************************************************************************************************************************************
# 4. Write a program to print the multiplication table of 9

print(" ")

n= 9
print("****************************** MULTIPLICATION TABLE OF" ,str(n),"***********************")
for i in range(1,11):
            print(n,"x",i,"=",n*i)


#************************************************************************************************************************************

# 5. Write a program to convert the number of days to ages

print(" ")
print("******************************* Convert the number of days to ages *********************************")
days=int(input("ENTER NUMBER OF DAYS:"))
age = days//365
print("AGE IS",age)

#*************************************************************************************************************************************

# 6. Check if a program is negative or positive

print(" ")
print("************************** Number is negative or positive ******************************")
number=int(input("ENTER A NUMBER:"))
if number > 0:
    print("NUMBER IS POSITIVE")
elif number == 0:
    print("NUMBER IS ZERO")
elif number < 0:
    print("NUMBER IS NEGATIVE")

#********************************************************************************************************************************************

# 7. Explain Armstrong number and write a code with a function

print(" ")
print("********************************* Armstrong number ********************************")

num = int(input("ENTER A NUMBER:"))
order = len(str(num))            #DECIDES HOW MANY TIMES EACH DIGIT HAS TO BE MULTIPLIED 
                                #len(str(num)) is important
sum = 0
temp = num
while temp > 0:             #TO FIND SUM OF ORDER OF EACH DIGIT
    digit = temp % 10
    sum += digit ** order
    temp = temp // 10

if num == sum:                        #DISPLAY
    print("THE GIVEN NUMBER IS AN ARMSTRONG NUMBER")
else:
    print("THE GIVEN NUMBER IS NOT AN ARMSTRONG NUMBER")
    
    

#**************************************************************************************************************************************************** 
    
# 8. Solve Trigonometry problem using math function write a program to solve using math function

print(" ")
print("Trigonometry problem using math function")
import math
def trignometry(n,m):
    if n == 'sin':
        return math.sin(m)
    elif n == 'cosin':
        return math.cosin(m)
    elif n == 'cos':
        return math.cos(m)
    elif n == 'cosec':
        return math.cosec(m)
    elif n == 'tan':
        return math.tan(m)
    elif n == 'cot':
        return math.cot(m)
print(trignometry('sin',90))

#**************************************************************************************************************************************************
# 9. Create a calculator only on a code level by using if condition (Basic arithmetic calculation)

print(" ")
print("******************* Basic arithmetic calculation ******************************")
while True:
    choice = input("ENTER YOUR CHOICE:")
    if choice in ("+","-","*","/"):
        num1=int(input("ENTER A NUMBER:"))
        num2=int(input("ENTER ANOTHER NUMBER:"))
        if(choice == "+"):
          print(num1,"+",num2,"=",num1+num2)
        elif(choice == "-"):
          print(num1,"-",num2,"=",num1-num2)
        elif(choice == "*" ):
          print(num1,"*",num2,"=",num1*num2)
        elif(choice == "/"):
          print(num1,"/",num2,"=",num1/num2)
    else:
        print("ENTER A VALID CHOICE")
        break
              
                
                       
#**************************************************************************************************************************************                      
    
    
    















         
