#DAY4

#1)Create three variables (a,b,c) to same value of any integer & do the following  a) Divide a by 10 b) Multiply b by 50 c) Add c value by 60

a=b=c=int(input("ENTER A NUMBER:"))
print(a,b,c)
a=a/10
print(a)
b=b*50
print(b)
c=c+60
print(c)
print("the value of a,b,c is " +  str(a) +" "+ str(b)+" " + str(c))

#2)Create a String variable of 5 characters and replace the 3rd character with G
print(" Create a String variable of 5 characters\t ")
st=input()
arr=[char for char in st]
arr[2]='G'
s=''.join(arr)
print(s)

#3)Create two values (a,b) of int,float data type & convert the vise versa 
a=int(input("enter a integer:"))
b=float(input("enter a float:"))
print(a)
print(b)
print(float(a))
print(int(b))






