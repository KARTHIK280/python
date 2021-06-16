#DAY5
#    1)	Write a program to create a list of n integer values and do the following:
	   	   	
#A)Add an item in to the list (using function):

nums=[1,3,2,4,5]
nums.append(6)
print(nums)

#B)Delete (using function):

nums.remove(6)
print(nums)


# C)Store the largest number from the list to a variable:

x=max(nums)
print(x)

#D)Store the Smallest number from the list to a variable:
y=min(nums)
print(y)

#*******************************************************************************************************************************

#2)Create a tuple and print the reverse of the created tuple:

hi=("hello",1,2,0.4)
print(hi[::-1])

#**************************************************************************************************************************
#3)Create a tuple and convert tuple into list:

hi=("hello",1,2,0.4)
y = list(hi)
print(y)
