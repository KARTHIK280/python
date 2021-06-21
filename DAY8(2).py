#DAY8(2)

# 6. Write a program to convert an integer to binary & octa decimal

print("Integer to binary & octal & decimal: ")
#convert an integer to binary & octal & decimal
n1=int(input("Enter integer:"))
print("Binary value of integer:",bin(n1))
print("Octal value of integer:",oct(n1))
print("Decimal value of integer:",n1)
 
#************************************************************************************************************************************

# 7. Write a Python program to check the sum of three elements and divided by avalue which is given as an input by the user:

print(" ")
print("Check the sum of three elements and divided by avalue which is given as an input by the user:")
#check the sum of three elements
a=int(input("Enter 1st element:"))
b=int(input("Enter 2nd element:"))
c=int(input("Enter 3rd element:"))
sum=a+b+c
print("Enter Element in which to be deleted:")
div=int(input())
divide=sum/div
print(divide)


#************************************************************************************************************************************

# 8. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.
 
print(" ")
print("First char have been changed to capital letter: ")
#get a string from a given string where all
strstr=input("Enter a string")
#occurrences of its first char have been changed to capital letter.
print(strstr.title())
 

#*******************************************************************************************************************************************

# 9. Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.

print(" ")
print("Change the first occurrence of the word to a user specified input: ")
#get a string from a given string(user input)
str=input("Enter a String as input:")    
#change the first occurrence of the word to a user specified input.
ch=list()
ch=list(str)
a=input("Enter Word to be replaced in the string")
ch[0]=a
str1="".join(ch)
print(str1)
 


#*********************************************************************************************************************************************

# 10.Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.


print(" ")
print("List number of items in a dictionary key and sort the list with the help of a function & without the function: ")
#list number of items in a dictionary key
n=int(input("Enter number of elements in dictionary:"))
d=dict()
for i in range(n,0,-1):
    d[i]=input()
print(d)
print("Number of items in dictionary key")
print(len(d.keys()))

#sorting dictionary
for i in sorted (d.keys()):
    print(i, end = " ")
 




















