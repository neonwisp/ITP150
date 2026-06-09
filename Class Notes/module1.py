""" 
Date Created: June 9, 2026
Review of print() function and string concatenation & inputs/outputs 1.2 in class

"""
print("Today is Monday") # edit 1, changed monday to Monday
print("Today", "is", "Monday", sep="...") # edit 2, changed monday to Monday

# end= is used to specify what should be printed at the end of the output. 
# By default, it is set to a newline character (\n), 
# which means that each print statement will be printed on a new line. 
# However, you can change this behavior by setting end= to a different string.
print("Today is Monday, ", end="") 
print("I like string beans.") 

# concepts in practice 2.
print("Hello", end=" ")
print("World!")

# input() function is used to get user input from the console.
# When you run this code, it will prompt the user to enter their first name, 
# and then it will print the name that was entered.
first_name = input("What is your first name? ") 
print(first_name)