import datetime

timestamp = datetime.date.fromtimestamp(1682350249)
print(timestamp)

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())

import datetime

now = datetime.datetime.now()

print (now)  # This is the datetime object
print (now.year) # prints only the year from the object
print (now.month) # prints only the month from the object
print (now.day) # prints only the day, as a number, from the object
print (now.hour) # prints only the hour (in UTC time)
print (now.minute) # prints only the minute
print (now.second) # prints only the second


# Finding the delta between two dates
past_date = datetime.datetime(2015, 3, 14, 9, 26)
print (past_date)
current_date = datetime.datetime.now()
delta = current_date - past_date
print (delta)

