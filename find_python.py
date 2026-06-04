"""
find_python.py
Author: ITP 150 Ashlee Raya
Date: June 2, 2026

This script prints the absolute directory path to the python executable and the
directory path to the Python installation using Python's sys library.
"""
import sys


# print the path to the Python executable
path_to_python_executable = sys.executable
print('The directory path to my Python executable is',
      path_to_python_executable)

# Print the path to the Python installation.
path_to_python_installation = sys.exec_prefix
print('The directory path to my Python installation is',
      path_to_python_installation)
