""" mixed_data_types.py 

Purpose:
this program demonstrates how to work with mixed data types in Python. It shows how to concatenate strings
and variables of different types, and how to convert between data types using the str() function.

lessons learned:
- Avoid hardcoding values when a variable already exists 
- Use descriptive variable names to make the code easier to read and understand
- Using variables makes code easier to modify and maintain.

Author: Ashlee Raya 
Date Created: June 12, 2026
"""
# ------------------------
# Version 1 (works)
# ------------------------

num = 2 
y = input()

print('2' + '.' + str(y)) 

# Problem:  
# The value 2 is hardcoded as a string in the print statement. meaning num is not being used in the print statement.
# Because '2' is baked into the print statement as a string, if someone decided 
# If one wants to change the value of num to 3, the output would still be EX. '2.345' instead of '3.345'. 


# ------------------------
# Version 2 (improved)
# ------------------------

num = 7 
digits = input() 

decimal_num = str(num) + '.' + digits 
print(decimal_num) 

# Improvements:
# I change the code to use the variable num instead of hardcoding the string '2'.
# Variable name changed to digits to be more descriptive
# This also allows for easier inspection of the code and debugging if necessary.