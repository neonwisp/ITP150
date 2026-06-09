""" 
Date Created: June 9, 2026
Review of print() function and string concatenation in class

"""
print("Today is Monday") # edit 1, changed monday to Monday
print("Today", "is", "Monday", sep="...") # edit 2, changed monday to Monday

# end= is used to specify what should be printed at the end of the output. 
# By default, it is set to a newline character (\n), 
# which means that each print statement will be printed on a new line. 
# However, you can change this behavior by setting end= to a different string.
print("Today is Monday, ", end="") 
print("I like string beans.") 