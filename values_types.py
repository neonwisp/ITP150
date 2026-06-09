"""
values_types.py
Author: ITP 150 Ashlee Raya
Date Created: June 8, 2026
This program demonstrates the use of different data types in Python, including integers, floats, and strings. It also shows how to determine the data type of a variable using the `type()` function.
"""
# values are determined by their data type, integer, float, and string
int_a = 10 
float_a = 10.0
string_a = "10"

# The `type()` function is used to determine the data type of a variable
# When you run this code, it will output the value of each variable along with its corresponding data type.

print(          # 1. opened 3 parentheses 1. for grouping
    int_a,  (   # 2. extra grouping function
        type(
             int_a
        ))      # 3. closes type() and the extra grouping function
)               # 4. closes print

# This code isnt wrong, but it is unnecessarily complex. It can be formatted to the following:
print(float_a, type(float_a)) # deleted the extra grouping function and parentheses
print(string_a, type(string_a))

# It is now formatted in a more straightforward way, making it easier to read and understand.