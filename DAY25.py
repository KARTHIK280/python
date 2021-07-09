#DAY25
# 1.	Write a Python program to convert a string to datetime
import datetime
print(" convert a string to datetime ")
def convert(date_time):
    format = '%b %d %Y %I:%M%p'
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str
date_time = 'Mar 24 2021 03:24PM'
print(convert(date_time))

# 2.	Write a Python program to subtract five days (last working day) from current date
print(" ")
print("subtract five days (last working day) from current date")
date = datetime.date.today()
days = datetime.timedelta(5)
new_date = date - days
print(new_date)

# 3.	Write a Python program to convert the date to datetime using a function
print(" ")
print("convert the date to datetime using a function")
def sample(date3):
    print(datetime.datetime.combine(date3, datetime.datetime.min.time()))
print("Converting date to datetime")
date3 = datetime.date.today()
sample(date3)


 # 4.	Write a Python program to print next 7 days (week) starting from today

print(" ")
print("print next 7 days (week) starting from today")
today = datetime.date.today()
for x in range(1,8):
    val = today + datetime.timedelta(days=x)
    print(val.strftime("%A"))