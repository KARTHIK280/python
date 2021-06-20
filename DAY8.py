#DAY8

# 1. Write a Python script to merge two Python dictionaries:
print("Python script to merge two Python dictionaries:")
a={"1":"one","2":"two"}
b={"3":"three","4":"four"}
a.update(b)                            #COMMAND TO MERGE TWO PYTHON DICTIONARIES
print(a)
print("")
#*************************************************************************************************************************************************************
 
# 2. Write a program to sort the value from descending to ascending in list and convert it in to a set:

print("Sort the value from descending to ascending in list and convert it in to a set:")
nums=[8,7,6,5,4,3,2,1]
temp=0
print(nums)


for i in range(0,len(nums)):             #SORTING 
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
                   temp=nums[i]
                   nums[i]=nums[j]
                   nums[j]=temp

                   
print("ELEMENTS SORTED IN ASCENDING ORDER:")
for i in range(0,len(nums)):            # DISPLAYING AFTER SORTING 



 nums=set(nums)                         # Convert list in to a set:
print(nums)
print()


#********************************************************************************************************************************************************************
# 3. Write a Python program to find the repeated items of a list:
print("Python program to find the repeated items of a list:")
l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
         print(i,end=",")

 

#*****************************************************************************************************************************************************************
# 4. Python program to swap cases of a given string.

print("\n ")                                           
print(" Swap cases of a given string:")
def swap_string(s1):
    result_str = ""
    for item in s1:
        if item.isupper():
            result_str += item.lower()
        else:
            result_str += item.upper()
    return result_str
print(swap_string("hIfI"))



#**********************************************************************************************************************************************************************
# 5. Write a Python program to find the Mean,median,mode among three given numbers
print(" ")
print("Mean,median,mode :")

num=[8,6,8]
n=len(num)

print("MEAN:")
#mean:
mean=sum(num)//n
print(mean)


print("MEDIAN:")
#median:

num.sort()
  
if n % 2 == 0:
    median1 = num[n//2]
    median2 = num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median =  num[n//2]
print(median) 
 

  
print("MODE:")
#MODE
from collections import Counter
data = Counter(num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)


#**********************************************************************************************************************************************************************













           
      
                                      
