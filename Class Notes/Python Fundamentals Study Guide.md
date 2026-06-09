Python Fundamentals Study Guide

This guide covers essential Python concepts, focusing on environment setup, basic input/output operations, and variable handling. Mastery of these topics is crucial for success.

I. Environment Setup & Navigation
                
A. Cyber Range Environment
- Purpose: A virtual environment pre-configured with necessary tools like VS Code and Firefox for Python development.
- Access: Log in to Cyber Range.
- Password Saving: Easier to save your password within Cyber Range to avoid re-entering.

- VS Code Launch:
    - Application Menu: Look - for "VS Code" in the applications.
    - Terminal Command: Type code in the terminal to launch VS Code.
    - VS Code Password: The password for VS Code is code.

B. Terminal Commands (Linux-based)

- ls: Lists all files and directories in the current location.
    - ls -a: Shows all files, including hidden files.
    - ls -l: Lists files with detailed information (permissions, type, size, etc.).
    - ls -al: Combines both -a and -l for a comprehensive list.

- clear: Clears the terminal screen.
- cd <directory_name>: Change Directory. Navigates into a specified directory.
    - Case Sensitivity: Directory names are case-sensitive (e.g., Desktop is different from desktop).
    - Example: cd Desktop (if Desktop is capitalized).
- chmod +x <filename.py>: Change Mode; grants execute permission to a Python file.

    - +x: Adds execute permission for all users.
    - Necessity: Without execute permission, you cannot run the Python file directly from the terminal.
- mkdir <directory_name>: Make Directory. Creates a new directory.
    - Example: mkdir ITP150

C. Visual Studio Code (VS Code)

- Opening Terminal: Press Ctrl + ` (backtick/tilde key, usually above Tab).

- Opening a Folder:
    - Go to File -> Open Folder.
    - Navigate to the desired directory (e.g., Desktop/ITP150).
    - Select the folder and click Select.
- Opening a Python File: Once a folder is open, click on the .py file in the left sidebar (e.g., Module1.py).
- Saving Files: Press Ctrl + S or go to File -> Save.
- Running Python Code: Click the "Play" button (often a green triangle) in the top right corner of the VS Code editor when a Python file is open.
- AI Suggestions (e.g., GitHub Copilot): If prompted to sign in or use AI suggestions, close them. We are not using AI support for this course.
- Python Extension: If prompted, install the recommended Python extension.

II. Basic Python Operations

A. print() Function

- Purpose: Displays output to the console.
- Syntax: print(<value1>, <value2>, ..., 
- sep='<separator>', end='<end_string>')
Arguments:

    - values: Can be strings (enclosed in single or double quotes), numbers, variables, etc.

            - sep (separator):

- Default: A single space (' ') separates multiple values printed in a single print() call. 
- Customization: You can change the separator (e.g., sep='-' will separate values with a hyphen).
- Example: print("Hello", "World", sep='-') outputs Hello-World.

        - end (end string):

- Default: A newline character (\n), meaning the next print() statement will start on a new line.
- Customization: You can specify what character(s) should appear at the end of the output.
- Effect: If end='' (an empty string), the next print() statement will continue on the same line.
- Example: print("Today is Monday", end='...') followed by print("I like string beans.") will output Today is Monday...I like string beans..
- Adding Characters: end='%%' will add %% at the end of the line.


 - String Literals: Text enclosed in single (' ') or double (" ") quotation marks.
- Concatenation vs. Separate Arguments:
    - print("Hello" + "World") concatenates strings directly.
    - print("Hello", "World") prints "Hello" and "World" separated by the default space.
- Syntax Errors:
    - Missing Quotes: print(Hello world) will result in a SyntaxError because Hello and world are not recognized as variables or strings.
    - Unmatched Parentheses: print("Hello World" will result in a SyntaxError.
- Output Verification:
    - Desired Output: Compare the program's output with the expected result.
    - Error Messages: Look for SyntaxError, NameError, ValueError in the terminal.

B. input() Function

Purpose: Prompts the user for input and reads it from the console.
Syntax: variable_name = input("Prompt message: ")
Components:
variable_name: A name chosen by the programmer to store the user's input.
input(): The function that pauses program execution, displays the prompt, and waits for user entry.
"Prompt message: ": A string displayed to the user, instructing them what to enter.
Storing Input: The user's input is stored as a string in the specified variable_name.
Example:
first_name = input("What is your first name? ")
print(first_name)
 When run, it will display "What is your first name? ", wait for user input, and then print the entered name.
III. Variables
A. Definition
Variable: A named storage location in the computer's memory (RAM) that holds a value.
Memory Address: Each variable is linked to a specific memory address (e.g., 0x12ABCD). Python handles this internally, allowing you to refer to data by its human-readable name.
B. Naming Conventions
No Spaces: Variable names cannot contain spaces.
Incorrect: first name = "John" (Python will treat first and name as separate entities, leading to errors).
Underscore for Multiple Words: Use an underscore (_) to separate words in a variable name for readability.
Correct: first_name = "John"
Reusability: Variables allow you to store and reuse data throughout your program without hard-coding values. This is essential for dynamic programs (e.g., user logins, changing data).
DRY Principle: Don't Repeat Yourself. Variables promote this by allowing you to store a value once and refer to it by name multiple times.
IV. Important Facts to Memorize
VS Code Launch Command: code
VS Code Password: code
Open VS Code Terminal: Ctrl + `
Change Directory Command: cd
List Files Command: ls
Grant Execute Permission: chmod +x <filename.py>
Create Directory Command: mkdir
Save File in VS Code: Ctrl + S
Default print() separator: A single space (' ')
Default print() end character: Newline (\n)
Variable Naming Rule: No spaces; use underscores for multiple words (e.g., my_variable).
input() function returns data as a: String.
Purpose of end='' in print(): To prevent a newline and continue output on the same line.
Purpose of sep='' in print(): To remove the default space separator between printed items.
DRY Principle: Don't Repeat Yourself.
Python is case-sensitive for commands, file names, and variable names.