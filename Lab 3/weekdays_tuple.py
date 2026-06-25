"""
weekdays_tuple.py
Author: ITP 150 Ashlee Raya
Date Created: June 6, 2026
This script creates a tuple with the days of the week, prints its contents, 
type, id, and length of the list. Then, change an element within the list,
and print its contents to verify if the change was made. Then print the id of
the list to prove that a list is mutable.
"""

weekdays = ('Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat')

print(weekdays)
print(type(weekdays))
print(id(weekdays))
print(len(weekdays))

# abbreviations should be 3 characters. Change Thur to Thu
# Initializing a tuple with 1 item. The , is required so that Python
# recognizes thu as a tuple with 1 item.
thu = ('Thu',)
print(type(thu))
# Create a new tuple with same name as old tuple but it will have a different
# object ID. 
weekdays = weekdays[:4] + thu + weekdays[5:7]

print(weekdays)
print(id(weekdays))
