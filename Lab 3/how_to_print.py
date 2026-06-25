"""
how_to_print.py
Author: ITP 150 Ashlee Raya
Date Created: June 6, 2026
This script shows how to print in Python with simple print
statements, the format() function, f strings, and format specifiers.
"""

my_float = 123_456.789  # Use _ to separate hundreds from thousands, etc.
my_integer = 123_456
my_string = 'ITP 150'
my_boolean = False

print('\nMethod 1: print() function with arguments separated by commas.')
print('The value of my float is', my_float, '.')
print('The value of my integer is', my_integer, '.')
print('The value of my string is', my_string, '.')
print('The value of my boolean is', my_boolean, '.')

print('\nMethod 2: print() function using concatenation +.')
print('The value of my float is ' + str(my_float) + '.')
print('The value of my integer is ' + str(my_integer) + '.')
print('The value of my string is ' + my_string + '.')
print('The value of my boolean is ' + str(my_boolean) + '.')

print('\nMethod 3: print f string formatting with {} placeholders. Preferred.')
# ,.2f means print a float with 2 decimal places and a comma separator.
print(f'The value of my float is {my_float:,.2f}.')
# ,d means print an integer with a comma separator
print(f'The value of my integer is {my_integer:,d}.')
print(f'The value of my string is {my_string}.')
print(f'The value of my boolean is {my_boolean}.')

print('\nMethod 3: print f string formatting with {} placeholders. Preferred.')
# ,.2f means print a float with 2 decimal places and a comma separator.
print(f'The value of my float is {my_float:,.2f}.')
# ,d means print an integer with a comma separator
print(f'The value of my integer is {my_integer:,d}.')
print(f'The value of my string is {my_string}.')
print(f'The value of my boolean is {my_boolean}.')
print('The value of my boolean is ', format(my_boolean), '.')

print('\nMethod 5. print using old string formatting with % operator.')
# https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting
print('This shows how to print using embedded formatting codes:')
print('The value of my float is %.2f.' % (my_float))  # f for float
print('The value of my integer is %d.' % (my_integer))  # d for integer
print('The value of my string is %s.' % (my_string))  # s for string
print('The value of my boolean is %s.' % (my_boolean))

print('\nMethod 6. print using old string formatting to create columns.')
# %-20s creates the 1st column 20 characters wide that is left aligned bc of -
# %20s creates the 2nd column 20 characters wide. s means string.
print('%-20s%20s' % ('Types of Data', 'Values Entered'))
# %20.2f creates 2nd column for float f specifying 2 decimal places precision.
print('%-20s%20.2f' % ('My Float', my_float))
# %20d creates 2nd column for My Integer d.
print('%-20s%20d' % ('My Integer', my_integer))
print('%-20s%20s' % ('My String', my_string))
print('%-20s%20s' % ('My Boolean', my_boolean))

print('\nMethod 7. print f string formatting to create columns. Preferred')
# > means right align. floats and integers right align by default.
# < means left align. strings left align by default.
# ^ means center align
# My Boolean data type must be cast as str if you want to see False or True.
# If you don't cast as a str, the output will show 0 for False, 1 for True.
print(f'{"Types of Data":20s}{"Values Entered":>20s}')
print(f'{"My Float":20s}{my_float:20,.2f}')
print(f'{"My Integer":20s}{my_integer:20,d}')
print(f'{"My String":20s}{my_string:>20s}')
print(f'{"My Boolean":20s}{str(my_boolean):>20}')