"""
code_to_debug.py
Author: ITP 150 Ashlee Raya     # Error 9, added author name 
Date Created: March 29, 2025
This program contains numerous errors and we will go through the process
of debugging it relying on syntax highlighting and reading tracebacks.
"""

first_release = 'February 20, 1991' #Error 1, 1st to first
creator = 'Guido van Rossum' #Error 2, changed " to '
organization = 'Python Software Foundation' #Error 3, added ' before Python
#Error 5, changes == to =, to organization
print('Python was first released on ' + first_release + '.') #Error 4, changed 1st to first
print('Python was created by', creator + '.')  #Error 6, change prnt to print
#Error 7, cretor to creator
print('Python is maintained by the', organization + '.')
#Error 8, seperated the organization variable from the literal strings. 
