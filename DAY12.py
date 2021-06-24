#DAY12

# 1. Create a file 30 days 30 hour operations
# 2. Write data in it I have completed 10 days successfully.
# 3. Append the data your name in to it.
# 4. Close the file.


file1=open("30 days 30 hour operations.txt","a")
n=input("enter name:")
file1.write(n)
print("name has appended sucessfully")
file1.close()
