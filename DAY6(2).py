#DAY6

# 1. Write a Python script to merge two Python dictionaries:

a={"MAHARASHTRA":"MUMBAI","TN":"CHENNAI"}
b={"KARNATAKA":"BANGLORE","BIHAR":"PATNA"}
a.update(b)        #merge two Python dictionaries
print(a)

# 2. Write a Python program to remove a key from a dictionary:
a={"MAHARASHTRA":"MUMBAI","TN":"CHENNAI","KARNATAKA":"BANGLORE","BIHAR":"PATNA"}
del a["MAHARASHTRA" ]           #delete a key value
print(a)


# 3. Write a Python program to map two lists into a dictionary:
state=["MAHARASHTRA","TN"]
capital=["MUMBAI","CHENNAI"]
india=dict(zip(state,capital))         #map two list
print(india)  
           

# 4. Write a Python program to find the length of a set:
set1={1,2,3,4,5}
set1.add(6)
print(set1)
print(len(set1))         #printing len of sets

# 5. Write a Python program to remove the intersection of a 2nd set from the 1st set:

s1={1,2,3,4,5}
s2={5,7,8,3,10}
print(s1.intersection(s2))            #intersecting 2 sets
print(s1.difference(s2))       #differencing two sets
