"""
 weekdays_list.py
 Author: ITP 150 Ashlee Raya
 Date Created: June 6, 2026
 This script creates a list with the days of the week, prints its contents, 
 type, id, and length of the list. Then, change an element within the list,
 and print its contents to verify if the change was made. Then print the id of
 8 the list to prove that a list is mutable.
 9 """

weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']

print(weekdays)
print(type(weekdays))
print(id(weekdays))
print(len(weekdays))

# abbreviations should be 3 characters. Change Thur to Thu
weekdays[4] = 'Thu'

print(weekdays)
print(id(weekdays))