#DAY21

# 1. Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
print(" *********** zip() function and list() function *********** ")
a=("lion","tiger")
b=("king","soldier")
c=zip(a,b)
print(list(c))

# 2. First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples
print(" ")
print(" ********************* Using zip, merge and create a tuple ***************")
x=list(range(1,9))
y=list(range(101,109))
print(x)
print(y)
final=tuple(zip(x,y))
print(final)

# 3. Using sorted() function, sort the list in ascending order.
print(" ")
print(" *********** sorted() function ************* ")
a1=[28,45,65,95,12,24]
a2=sorted(a1)
print(a2)

# 4. Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

print(" ")
print("***************************** filter the even numbers so that only odd numbers are passed to the new list ************* ")
def filtereven(nums):
    if nums%2 ==0:
        return False
    else:
        return True

num=[28,45,65,95,12,24]
final2=filter(filtereven,num)
for i in final2:
    print(i)
       

 
